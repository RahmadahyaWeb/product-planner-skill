#!/usr/bin/env python3
"""Cek keterlacakan artefak app-product-planner (stdlib saja).

Pemakaian:
  python check_artifacts.py <folder-perencanaan> [--json]
  python check_artifacts.py <folder-perencanaan> --next [N]
  python check_artifacts.py --self-test

--next: cetak N task terbuka berikutnya (bukan BLOCKED, semua Dep sudah [x]) beserta
pointer file:line ke definisi ID yang dirujuk. Untuk melanjutkan implementasi di sesi
baru tanpa membaca semua artefak.

Mencocokkan ID secara tekstual:
  - FR di PRD.md yang tidak disebut di PLAN.md (FR bertanda "Tidak" di tabel = non-UI, dilaporkan terpisah)
  - SCR di PLAN.md tanpa file prototype (prototype wajib) (nama file scr-xxx, atau ID disebut di file non-.md di prototype/)
  - SCR tanpa wireframe (heading di UI.md), COMP di UI.md tanpa SCR pemakai
  - FR, SCR, dan COMP yang tidak disebut di implementation.md
  - Jumlah task - [ ] / - [x] / BLOCKED di implementation.md
"""
import json
import re
import sys
import tempfile
from pathlib import Path

FR_RE = re.compile(r"\bFR-\d{3,}\b")
SCR_RE = re.compile(r"\bSCR-\d{3,}[a-z]?(?:-(?:[a-z]+))?\b")
COMP_RE = re.compile(r"\bCOMP-\d{3,}\b")
STRUCK_RE = re.compile(r"~~\s*((?:FR|SCR|COMP)-\d{3,}[a-z]?)\s*~~")
HEADER_RE = re.compile(r"(?:<!--|/\*|//)\s*(SCR-\d{3,}[^\n]*)")
TASK_RE =re.compile(r"^\s*[-*] \[( |x|X)\] \*\*(TASK-\d{3,})")
REF_RE = re.compile(r"\b(?:FR|NFR|SCR|COMP)-\d{3,}[a-z]?\b")
DEP_RE = re.compile(r"Dep(?:endensi)?\W*([^\u00b7\n]*)")
TASK_ID_RE = re.compile(r"\bTASK-\d{3,}\b")
DEF_FILE = {"FR": ["PRD.md"], "NFR": ["PRD.md"], "SCR": ["PLAN.md", "UI.md"], "COMP": ["UI.md"]}


RANGE_RE = re.compile(r"\b(FR|NFR|SCR|COMP)-(\d{3,})\s*(?:\.\.|–|—)\s*(?:\1-)?(\d{3,})\b")


def expand_ranges(text: str) -> str:
    """Tambahkan ID di dalam rentang "COMP-001..COMP-009" agar ikut terhitung."""
    extra = [f"{p}-{n:0{len(a)}d}" for p, a, b in RANGE_RE.findall(text)
             for n in range(int(a), int(b) + 1) if int(b) - int(a) < 200]
    return text + ("\n" + " ".join(extra) if extra else "")


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace") if p.is_file() else ""


def ids(regex, text, struck):
    return {m for m in regex.findall(text)} - struck


def non_ui_frs(prd: str) -> set:
    """FR yang barisnya di tabel PRD punya sel 'Tidak' (kolom Butuh UI)."""
    out = set()
    for line in prd.splitlines():
        s = line.strip()
        if s.startswith("|"):
            m = FR_RE.search(s.split("|")[1] if s.count("|") > 1 else "")
            cells = [c.strip().lower() for c in s.strip("|").split("|")]
            if m and ("tidak" in cells or "no" in cells):
                out.add(m.group(0))
    return out


def check(root: Path) -> dict:
    prd = read(root / "PRD.md")
    ux = read(root / "PLAN.md")
    impl_path = root / "implementation.md"
    impl = expand_ranges(read(impl_path))
    ui_path = root / "UI.md"
    ui = read(ui_path)
    struck = set(STRUCK_RE.findall(prd + ux + ui))
    comps = ids(COMP_RE, ui, struck)
    wireframed = {i for l in ui.splitlines() if l.lstrip().startswith("#") for i in SCR_RE.findall(l)}
    comp_unused = sorted({m.group(0) for l in ui.splitlines() if l.strip().startswith("|")
                          for m in [COMP_RE.search(l.split("|")[1])] if m
                          and not SCR_RE.search(l) and not re.search(r"\b(semua|all)\b", l, re.I)} - struck)

    frs = ids(FR_RE, prd, struck)
    non_ui = non_ui_frs(prd) & frs
    scrs = ids(SCR_RE, ux, struck)
    ux_frs = ids(FR_RE, ux, struck)

    proto_dir = root / "prototype"
    proto_hits = set()
    if proto_dir.is_dir():
        for f in proto_dir.rglob("*"):
            if not f.is_file() or f.suffix.lower() == ".md":
                continue
            m = re.search(r"scr-(\d{3,}[a-z]?)", f.name, re.I)
            if m:
                proto_hits.add("SCR-" + m.group(1).lower())
            # Halaman mengklaim ID lewat komentar header: <!-- SCR-002 Kasir + SCR-002a Modal | FR-... -->
            # Hanya bagian sebelum "|" yang dihitung, agar index/daftar tautan tidak dianggap prototype.
            for claim in HEADER_RE.findall(read(f)):
                proto_hits |= set(SCR_RE.findall(claim.split("|")[0]))

    tasks = []
    for line in impl.splitlines():
        m = TASK_RE.match(line)
        if m:
            tasks.append({"id": m.group(2), "done": m.group(1).lower() == "x", "blocked": "BLOCKED" in line.upper()})
    impl_frs = ids(FR_RE, impl, set())
    impl_scrs = ids(SCR_RE, impl, set())
    task_ids = [t["id"] for t in tasks]

    return {
        "files": {n: (root / n).exists() for n in ["PRD.md", "PLAN.md", "UI.md", "implementation.md"]},
        "fr_total": len(frs),
        "fr_non_ui": sorted(non_ui),
        "fr_ui_without_scr_mention": sorted(frs - non_ui - ux_frs),
        "scr_total": len(scrs),
        "prototype_exists": proto_dir.is_dir(),
        "scr_without_prototype": sorted(scrs - proto_hits),
        "scr_without_wireframe": sorted(scrs - wireframed) if ui_path.is_file() else None,
        "comp_total": len(comps),
        "comp_unused": comp_unused,
        "impl_exists": impl_path.is_file(),
        "fr_without_task": sorted(frs - impl_frs) if impl else [],
        "scr_without_task": sorted(scrs - impl_scrs) if impl else [],
        "comp_without_task": sorted(comps - ids(COMP_RE, impl, set())) if impl else [],
        "tasks_total": len(tasks),
        "tasks_done": sum(t["done"] for t in tasks),
        "tasks_blocked": sorted(t["id"] for t in tasks if t["blocked"]),
        "duplicate_task_ids": sorted({t for t in task_ids if task_ids.count(t) > 1}),
    }


def task_blocks(impl: str) -> list:
    """Blok task: baris judul + sub-bullet ber-indent sampai task/heading/baris tanpa indent berikutnya."""
    blocks, cur = [], None
    for line in impl.splitlines():
        m = TASK_RE.match(line)
        if m:
            cur = {"id": m.group(2), "done": m.group(1).lower() == "x",
                   "blocked": "BLOCKED" in line.upper(), "lines": [line]}
            blocks.append(cur)
        elif cur and line.strip() and line[:1] in " \t" and not line.lstrip().startswith("#"):
            cur["lines"].append(line)
        else:
            cur = None
    return blocks


def def_line(root: Path, ref: str, cache: dict):
    """file:line definisi ID di tiap file definisinya (SCR: PLAN.md + wireframe di UI.md)."""
    out = [_def_line(root, ref, f, cache) for f in DEF_FILE[ref.split("-")[0]]]
    if ref.startswith("SCR-"):
        out += [str(f.relative_to(root)) for f in sorted((root / "prototype").rglob(f"{ref.lower()}-*.html"))]
    return ", ".join(out)


def _def_line(root: Path, ref: str, fname: str, cache: dict):
    """Utamakan baris yang diawali ID (heading/tabel/bullet), lalu sebutan pertama."""
    if fname not in cache:
        cache[fname] = read(root / fname).splitlines()
    first = None
    for i, line in enumerate(cache[fname], 1):
        if re.search(rf"\b{re.escape(ref)}\b", line):
            if line.lstrip("#|*- \t").startswith(ref):
                return f"{fname}:{i}"
            first = first or f"{fname}:{i}"
    return first or f"{fname}: (tidak ditemukan)"


def next_tasks(root: Path, n: int = 1) -> str:
    impl = read(root / "implementation.md")
    if not impl:
        return "implementation.md tidak ada."
    blocks = task_blocks(impl)
    done = {b["id"] for b in blocks if b["done"]}
    out, skipped, picked = [], [], 0
    progres = [l for l in impl.splitlines()[:15] if "progres" in l.lower()]
    out.append(f"Task: {len(done)} selesai / {len(blocks)} total")
    out += progres
    for b in blocks:
        if b["done"] or picked >= n:
            continue
        text = "\n".join(b["lines"])
        if b["blocked"]:
            skipped.append(f"{b['id']} (BLOCKED)")
            continue
        deps = {t for m in DEP_RE.findall(text) for t in TASK_ID_RE.findall(m)} - done
        if deps:
            skipped.append(f"{b['id']} (tunggu {', '.join(sorted(deps))})")
            continue
        picked += 1
        cache = {}
        out += ["", text, "Definisi ID:"]
        out += [f"  {r} -> {def_line(root, r, cache)}" for r in sorted(set(REF_RE.findall(expand_ranges(text))))] or ["  (tidak ada)"]
    if not picked:
        out.append("\nTidak ada task terbuka yang siap dikerjakan.")
    if skipped:
        out.append("Dilewati: " + "; ".join(skipped))
    return "\n".join(out)


def show(r: dict) -> str:
    def lst(x):
        return ", ".join(x) if x else "tidak ada"
    lines = ["Artefak: " + ", ".join(f"{k}{'' if v else ' (TIDAK ADA)'}" for k, v in r["files"].items())]
    lines.append(f"FR: {r['fr_total']} (non-UI: {lst(r['fr_non_ui'])})")
    lines.append(f"FR UI tidak disebut di PLAN: {lst(r['fr_ui_without_scr_mention'])}")
    proto = f" | tanpa file prototype: {lst(r['scr_without_prototype'])}" + ("" if r["prototype_exists"] else " (folder prototype/ belum ada)")
    lines.append(f"SCR: {r['scr_total']}{proto}")
    if r["scr_without_wireframe"] is None:
        lines.append("UI.md belum ada (wireframe dan komponen wajib sebelum implementation.md).")
    else:
        lines.append(f"SCR tanpa wireframe: {lst(r['scr_without_wireframe'])}")
        lines.append(f"COMP: {r['comp_total']} | tanpa SCR pemakai: {lst(r['comp_unused'])}")
    if r["impl_exists"]:
        lines.append(f"Task: {r['tasks_done']} selesai / {r['tasks_total']} total | blocked: {len(r['tasks_blocked'])} ({lst(r['tasks_blocked'])})")
        lines.append(f"FR tanpa task: {lst(r['fr_without_task'])}")
        lines.append(f"SCR tanpa task: {lst(r['scr_without_task'])}")
        lines.append(f"COMP tanpa task: {lst(r['comp_without_task'])}")
        if r["duplicate_task_ids"]:
            lines.append(f"ID task duplikat: {lst(r['duplicate_task_ids'])}")
    else:
        lines.append("implementation.md belum ada.")
    return "\n".join(lines)


def self_test():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "PRD.md").write_text(
            "| ID | Req | Butuh UI? |\n|---|---|---|\n| FR-001 | a | Ya |\n| FR-002 | b | Tidak |\n| FR-003 | c | Ya |\n~~FR-004~~ dihapus\n",
            encoding="utf-8")
        (root / "PLAN.md").write_text("SCR-001 FR-001\nSCR-002 FR-001\nSCR-002a modal\nSCR-003 planned\nSCR-001-staff variasi\n", encoding="utf-8")
        assert not check(root)["prototype_exists"] and len(check(root)["scr_without_prototype"]) == 5
        assert check(root)["scr_without_wireframe"] is None
        (root / "UI.md").write_text(
            "### SCR-001 — Home\n### SCR-002 — List\n| ID | K | Dipakai |\n|---|---|---|\n"
            "| COMP-001 | Button | SCR-001 |\n| COMP-002 | Card | — |\n| COMP-003 | Footer | semua |\n",
            encoding="utf-8")
        u = check(root)
        assert u["scr_without_wireframe"] == ["SCR-001-staff", "SCR-002a", "SCR-003"], u
        assert u["comp_total"] == 3 and u["comp_unused"] == ["COMP-002"], u
        (root / "prototype" / "pages").mkdir(parents=True)
        (root / "prototype" / "pages" / "scr-001-home.html").write_text("<!-- SCR-001 -->", encoding="utf-8")
        (root / "prototype" / "pages" / "scr-002-list.html").write_text("<!-- SCR-002 List + SCR-002a Modal | FR-001 -->", encoding="utf-8")
        (root / "prototype" / "index.html").write_text("<!-- hub --><a>SCR-003 belum</a>", encoding="utf-8")
        (root / "prototype" / "README.md").write_text("SCR-003 not built", encoding="utf-8")
        (root / "implementation.md").write_text(
            "- [ ] **TASK-001 — x** FR-001 SCR-001\n- [x] **TASK-002 — y** FR-002\n- [ ] **TASK-003 — ⛔ BLOCKED: z** SCR-002\n",
            encoding="utf-8")
        r = check(root)
        assert r["fr_total"] == 3, r
        assert r["fr_non_ui"] == ["FR-002"], r
        assert r["fr_ui_without_scr_mention"] == ["FR-003"], r
        assert r["scr_total"] == 5 and r["scr_without_prototype"] == ["SCR-001-staff", "SCR-003"], r
        assert r["tasks_total"] == 3 and r["tasks_done"] == 1 and r["tasks_blocked"] == ["TASK-003"], r
        assert r["fr_without_task"] == ["FR-003"], r
        assert r["scr_without_task"] == ["SCR-001-staff", "SCR-002a", "SCR-003"], r
        assert r["comp_without_task"] == ["COMP-001", "COMP-002", "COMP-003"], r
        assert "COMP-002" in expand_ranges("COMP-001..COMP-003") and "FR-005" in expand_ranges("FR-004–006")
        (root / "prototype" / "pages" / "scr-002-list.html").unlink()
        assert check(root)["scr_without_prototype"] == ["SCR-001-staff", "SCR-002", "SCR-002a", "SCR-003"]
        (root / "implementation.md").write_text(
            "- [x] **TASK-001 — a** FR-001\n- [ ] **TASK-002 — ⛔ BLOCKED: b**\n"
            "- [ ] **TASK-003 — c** — Dep: TASK-002 · FR-001\n- [ ] **TASK-004 — d**\n"
            "  - **Referensi:** FR-003, SCR-001, COMP-001\n  - **Dependensi:** TASK-001\n## E\n",
            encoding="utf-8")
        nx = next_tasks(root)
        assert "TASK-004 — d" in nx and "**Referensi:** FR-003" in nx and "## E" not in nx, nx
        assert "TASK-002 (BLOCKED)" in nx and "TASK-003 (tunggu TASK-002)" in nx, nx
        assert "FR-003 -> PRD.md:5" in nx and "SCR-001 -> PLAN.md:1, UI.md:1, prototype/pages/scr-001-home.html" in nx and "COMP-001 -> UI.md:5" in nx, nx
    print("self-test OK")


def main(argv):
    if "--self-test" in argv:
        self_test()
        return 0
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    root = Path(args[0])
    if not root.is_dir():
        print(f"Folder tidak ditemukan: {root}")
        return 2
    if "--next" in argv:
        n = int(args[1]) if len(args) > 1 and args[1].isdigit() else 1
        print(next_tasks(root, n))
        return 0
    r = check(root)
    print(json.dumps(r, indent=2, ensure_ascii=False) if "--json" in argv else show(r))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
