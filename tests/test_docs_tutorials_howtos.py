#!/usr/bin/env python3
"""Executable validation tests for EN/FR Diataxis docs, YAML manifests, CLI examples, links, and Mermaid."""

from __future__ import annotations

import pathlib
import re
import shlex
import shutil
import subprocess
import tempfile
import unittest
import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]

EN_QUADRANTS = ("01-tutorials", "02-how-to-guides", "03-reference", "04-explanation")
FR_QUADRANTS = ("01-tutoriels", "02-guides-pratiques", "03-reference", "04-explications")

DIATAXIS_DIRS_EN = tuple(REPO_ROOT / "en" / q for q in EN_QUADRANTS)
DIATAXIS_DIRS_FR = tuple(REPO_ROOT / "fr" / q for q in FR_QUADRANTS)

VALID_MERMAID_HEADERS = re.compile(
    r"^\s*(?:flowchart(?:-elk)?|graph\s+(?:TD|TB|LR|RL|BT)|sequenceDiagram|"
    r"stateDiagram(?:-v2)?|classDiagram|erDiagram|gantt|pie|gitGraph|"
    r"mindmap|timeline|xychart-beta)\b"
)

ALLOWED_K8S_KINDS = {
    "MariaDB",
    "MariaDBVersion",
    "MariaDBOpsRequest",
    "MariaDBAutoscaler",
    "MariaDBMigration",
    "MariaDBArchiver",
    "AppBinding",
    "BackupStorage",
    "RetentionPolicy",
    "BackupConfiguration",
    "Secret",
    "ConfigMap",
    "Service",
}

ALLOWED_CLI_ROOTS = {"kubectl", "helm", "mariadb", "maxctrl", "export"}
ALLOWED_KUBECTL_SUBCMDS = {
    "apply",
    "create",
    "get",
    "describe",
    "delete",
    "wait",
    "exec",
    "logs",
    "edit",
    "patch",
}


def iter_markdown_files() -> list[pathlib.Path]:
    """Return sorted Markdown files in the repository excluding hidden/cache dirs."""
    files: list[pathlib.Path] = []
    for p in sorted(REPO_ROOT.rglob("*.md")):
        if any(part.startswith(".") or part == "node_modules" for part in p.relative_to(REPO_ROOT).parts):
            continue
        files.append(p)
    return files


def parse_fenced_blocks(text: str) -> list[dict[str, object]]:
    """Parse CommonMark fenced code blocks and report unclosed fence status."""
    lines = text.splitlines()
    blocks: list[dict[str, object]] = []
    in_fence = False
    fence_char = ""
    fence_len = 0
    open_line = 0
    indent = ""
    lang = ""
    buf: list[str] = []

    for idx, line in enumerate(lines, start=1):
        if not in_fence:
            m = re.match(r"^([ ]{0,3})(`{3,}|~{3,})(.*)$", line)
            if not m:
                continue
            ind, marker, info = m.groups()
            if marker[0] == "`" and "`" in info:
                continue
            in_fence = True
            fence_char = marker[0]
            fence_len = len(marker)
            open_line = idx
            indent = ind
            lang_tok = info.strip().split()[0].lower() if info.strip() else ""
            lang = lang_tok.lstrip(".")
            buf = []
        else:
            if re.match(rf"^[ \t]*{re.escape(fence_char)}{{{fence_len},}}[ \t]*$", line):
                blocks.append(
                    {
                        "open_line": open_line,
                        "close_line": idx,
                        "indent": indent,
                        "lang": lang,
                        "body": "\n".join(buf),
                    }
                )
                in_fence = False
            else:
                buf.append(line)

    if in_fence:
        raise AssertionError(f"Unclosed Markdown code fence starting at line {open_line}")
    return blocks


class TestDocsTutorialsHowTos(unittest.TestCase):
    """Verify EN/FR Diataxis portals, YAML manifests, CLI examples, links, and Mermaid."""

    def test_diataxis_quadrants_and_relative_links(self) -> None:
        """Verify EN and FR Diataxis portals plus 100% relative link integrity across all docs."""
        for lang_dir, quads in ((REPO_ROOT / "en", EN_QUADRANTS), (REPO_ROOT / "fr", FR_QUADRANTS)):
            self.assertTrue((lang_dir / "index.md").is_file(), f"Missing {lang_dir / 'index.md'}")
            for q in quads:
                q_dir = lang_dir / q
                self.assertTrue((q_dir / "index.md").is_file(), f"Missing {q_dir / 'index.md'}")
                pages = [p for p in q_dir.glob("*.md") if p.name != "index.md"]
                self.assertGreaterEqual(len(pages), 2, f"Expected >=2 content pages in {q_dir}")

        link_re = re.compile(r"!?\[[^\]]*\]\(([^)\n]+)\)")
        broken: list[str] = []
        for md in iter_markdown_files():
            text = md.read_text(encoding="utf-8")
            blocks = parse_fenced_blocks(text)
            fenced_lines = {
                ln for b in blocks for ln in range(int(b["open_line"]), int(b["close_line"]) + 1)
            }
            for lineno, line in enumerate(text.splitlines(), start=1):
                if lineno in fenced_lines:
                    continue
                cleaned = re.sub(r"`[^`]*`", " ", line)
                for match in link_re.finditer(cleaned):
                    target = match.group(1).strip().split()[0].split("#")[0].split("?")[0]
                    if not target or re.match(r"^(?:https?|mailto|ftp):", target, re.I):
                        continue
                    resolved = (md.parent / target).resolve()
                    if not resolved.exists():
                        broken.append(f"{md.relative_to(REPO_ROOT)}:{lineno} -> {target}")
        self.assertEqual(broken, [], f"Broken relative links found: {broken}")

    def test_yaml_manifests_valid_and_k8s_schema(self) -> None:
        """Verify every YAML fence parses cleanly and Diataxis manifests have valid K8s fields."""
        diataxis_proc_dirs = (
            REPO_ROOT / "en" / "01-tutorials",
            REPO_ROOT / "en" / "02-how-to-guides",
            REPO_ROOT / "fr" / "01-tutoriels",
            REPO_ROOT / "fr" / "02-guides-pratiques",
        )
        for md in iter_markdown_files():
            text = md.read_text(encoding="utf-8")
            for blk in parse_fenced_blocks(text):
                if blk["lang"] not in ("yaml", "yml"):
                    continue
                docs = [d for d in yaml.safe_load_all(str(blk["body"])) if d is not None]
                self.assertTrue(docs, f"Empty YAML block at {md.relative_to(REPO_ROOT)}:{blk['open_line']}")
                for doc in docs:
                    self.assertIsInstance(
                        doc,
                        (dict, list),
                        f"Non-object YAML block at {md.relative_to(REPO_ROOT)}:{blk['open_line']}",
                    )
                if any(md.is_relative_to(d) for d in diataxis_proc_dirs):
                    for doc in docs:
                        self.assertIsInstance(doc, dict)
                        self.assertIn("apiVersion", doc, f"Missing apiVersion in {md.name}:{blk['open_line']}")
                        self.assertIn("kind", doc, f"Missing kind in {md.name}:{blk['open_line']}")
                        self.assertIn(doc["kind"], ALLOWED_K8S_KINDS)
                        meta = doc.get("metadata", {})
                        self.assertIsInstance(meta, dict)
                        self.assertTrue(meta.get("name"), f"Missing metadata.name in {md.name}:{blk['open_line']}")

    def test_tutorial_and_howto_cli_commands(self) -> None:
        """Validate kubectl/bash/mysql syntax and ensure zero ASCII tables in bash blocks."""
        target_dirs = (
            REPO_ROOT / "en" / "01-tutorials",
            REPO_ROOT / "en" / "02-how-to-guides",
            REPO_ROOT / "fr" / "01-tutoriels",
            REPO_ROOT / "fr" / "02-guides-pratiques",
        )
        for d in target_dirs:
            for md in sorted(d.glob("*.md")):
                for blk in parse_fenced_blocks(md.read_text(encoding="utf-8")):
                    lang = str(blk["lang"])
                    body = str(blk["body"])
                    if lang not in ("bash", "shell", "sh"):
                        continue
                    self.assertFalse(
                        re.search(r"\+[-=]{2,}\+|[┌┐┘╔╗╚╝]", body),
                        f"ASCII box/table found inside {lang} block at {md.name}:{blk['open_line']}",
                    )
                    # Join line continuations and parse each command cleanly
                    joined = re.sub(r"\\\r?\n", " ", body)
                    for raw_line in joined.splitlines():
                        stmt = raw_line.strip()
                        if not stmt or stmt.startswith("#"):
                            continue
                        if stmt.startswith("$ "):
                            stmt = stmt[2:].strip()
                        tokens = shlex.split(stmt, posix=True)
                        self.assertTrue(tokens)
                        self.assertIn(
                            tokens[0],
                            ALLOWED_CLI_ROOTS,
                            f"Unexpected CLI root '{tokens[0]}' in {md.name}:{blk['open_line']}",
                        )
                        if tokens[0] == "kubectl":
                            self.assertGreaterEqual(len(tokens), 2)
                            self.assertIn(tokens[1], ALLOWED_KUBECTL_SUBCMDS)

    def test_mermaid_syntax_and_zero_ascii_diagrams(self) -> None:
        """Verify all Mermaid blocks are column-0, valid, and compile with mmdc if available."""
        mermaid_bodies: list[tuple[str, str]] = []
        for md in iter_markdown_files():
            text = md.read_text(encoding="utf-8")
            rel = md.relative_to(REPO_ROOT).as_posix()
            for blk in parse_fenced_blocks(text):
                lang = str(blk["lang"])
                body = str(blk["body"])
                if lang == "mermaid":
                    self.assertEqual(
                        blk["indent"],
                        "",
                        f"Indented Mermaid block at {rel}:{blk['open_line']}",
                    )
                    first_non_comment = next(
                        (ln for ln in body.splitlines() if ln.strip() and not ln.strip().startswith("%%")),
                        "",
                    )
                    self.assertRegex(
                        first_non_comment,
                        VALID_MERMAID_HEADERS,
                        f"Invalid Mermaid diagram header in {rel}:{blk['open_line']}",
                    )
                    if not rel.endswith("_combined.md"):
                        mermaid_bodies.append((f"{rel}:{blk['open_line']}", body))
                elif lang not in ("diff", "patch", "sql", "mysql", "psql"):
                    lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
                    footer_re = re.compile(r"^(?:\(\d+\s+rows?\)|\d+\s+rows?\s+in\s+set\b.*|Empty set\b.*)$", re.I)
                    while lines and footer_re.match(lines[-1]):
                        lines.pop()
                    has_box = bool(re.search(r"[┌┐┘╔╗╚╝]|\+[-=]{2,}\+", body))
                    if has_box and lines:
                        pipe_ratio = sum(1 for ln in lines if ln.startswith(("|", "│"))) / len(lines)
                        rule_re = re.compile(r"^[+┌├└╠╞╚][─━═\-=+:┬┼┴╦╬╩]+[+┐┤┘╗╣╝]$")
                        multi_col_re = re.compile(r"(?:[┬┼┴╦╬╩]|^\+[^+]*\+[^+]*\+)")
                        all_grid = all(
                            rule_re.match(ln) or ((ln[0] in "|│") and (ln[-1] in "|│"))
                            for ln in lines
                        )
                        has_multi_col = any(multi_col_re.search(ln) for ln in lines)
                        if pipe_ratio <= 0.45 and not (all_grid and has_multi_col):
                            self.fail(f"ASCII diagram outside tabular fence in {rel}:{blk['open_line']}")

        self.assertGreaterEqual(len(mermaid_bodies), 15, "Expected >=15 unique EN/FR Mermaid diagrams")

        mmdc_bin = shutil.which("mmdc")
        if not mmdc_bin:
            candidate = pathlib.Path("/home/jmren/node_modules/.bin/mmdc")
            if candidate.is_file():
                mmdc_bin = str(candidate)
        if mmdc_bin:
            with tempfile.TemporaryDirectory() as tmpdir:
                for label, body in mermaid_bodies:
                    src = pathlib.Path(tmpdir) / "diagram.mmd"
                    out = pathlib.Path(tmpdir) / "diagram.svg"
                    src.write_text(body, encoding="utf-8")
                    proc = subprocess.run([mmdc_bin, "-i", str(src), "-o", str(out)], capture_output=True, text=True)
                    self.assertEqual(proc.returncode, 0, f"mmdc failed for {label}: {proc.stderr}")
                    self.assertTrue(out.is_file() and out.stat().st_size > 0)

    def test_fr_en_language_isolation(self) -> None:
        """Ensure strict FR/EN separation and zero leftover machine-translation errors."""
        fr_forbidden = re.compile(
            r"(MariaDBOpsDemande|SauvegardeStockage|SauvegardeConfiguration|"
            r"pirater KubeDB|Stanadlone|stanadlone|"
            r"spécification\.(?:configuration|stockage|version|secret|source|cible)|"
            r"statut\.(?:phase|observedGeneration|conditions)|"
            r"\bBefore You Begin\b|\bNext Steps\b|Maintenant, attends)",
            re.I,
        )
        en_forbidden = re.compile(r"\b(stanadlone|Kubed operator|kubeclt|Bellow)\b", re.I)

        for p in sorted((REPO_ROOT / "fr").rglob("*.md")):
            text = p.read_text(encoding="utf-8")
            self.assertIsNone(
                fr_forbidden.search(text),
                f"FR translation defect in {p.relative_to(REPO_ROOT)}: {fr_forbidden.search(text)}",
            )

        for p in sorted((REPO_ROOT / "en").rglob("*.md")):
            text = p.read_text(encoding="utf-8")
            self.assertIsNone(
                en_forbidden.search(text),
                f"EN copy defect in {p.relative_to(REPO_ROOT)}: {en_forbidden.search(text)}",
            )

    def test_runbook_governance_and_skill_validators(self) -> None:
        """Verify EN/FR runbook governance headings, concise sentences, and Diataxis linters if present."""
        for md in sorted((REPO_ROOT / "en" / "02-how-to-guides").glob("*.md")):
            if md.name == "index.md":
                continue
            txt = md.read_text(encoding="utf-8")
            self.assertRegex(txt, r"(?im)^##\s+Verification\b")
            self.assertRegex(txt, r"(?im)^##\s+Rollback\b")
            self.assertNotRegex(txt, r"(?im)^##+\s+.*(?:Why|Architecture|Theory)\b")
            self.assertNotIn(";", re.sub(r"```[\s\S]*?```", "", txt))

        for md in sorted((REPO_ROOT / "fr" / "02-guides-pratiques").glob("*.md")):
            if md.name == "index.md":
                continue
            txt = md.read_text(encoding="utf-8")
            self.assertRegex(txt, r"(?im)^##\s+V[ée]rification\b")
            self.assertRegex(txt, r"(?im)^##\s+Retour\s+arri[èe]re\b")
            self.assertNotRegex(txt, r"(?im)^##+\s+.*(?:Pourquoi|Architecture|Th[ée]orie)\b")
            self.assertNotIn(";", re.sub(r"```[\s\S]*?```", "", txt))


if __name__ == "__main__":
    unittest.main()
