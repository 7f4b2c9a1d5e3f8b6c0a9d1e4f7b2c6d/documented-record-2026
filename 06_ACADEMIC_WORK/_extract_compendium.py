#!/usr/bin/env python3
"""Extract unified compendium from MCP JSON and split into Volume packages."""
from __future__ import annotations

import json
import re
from pathlib import Path

MCP = Path(
    r"C:\Users\murra\.grok\sessions\C%3A%5CUsers%5Cmurra\019fcd00-5004-7563-b643-921bc5af7240"
    r"\mcp\call-04d5da5f-e0f4-43fb-b0b1-3c0ddc7de4f7-18.json"
)
MCP_V1 = Path(
    r"C:\Users\murra\.grok\sessions\C%3A%5CUsers%5Cmurra\019fcd00-5004-7563-b643-921bc5af7240"
    r"\mcp\call-04d5da5f-e0f4-43fb-b0b1-3c0ddc7de4f7-19.json"
)
BASE = Path(r"C:\Users\murra\code\documented-record-2026\06_ACADEMIC_WORK")
COMP = BASE / "compendium"
SUB = BASE / "journal_submissions"


def load_content(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = None
    if isinstance(data, dict):
        c = data.get("content")
        if isinstance(c, str) and len(c) > 100:
            return c
        if isinstance(c, list):
            parts = []
            for item in c:
                if isinstance(item, dict) and "text" in item:
                    parts.append(item["text"])
                else:
                    parts.append(str(item))
            joined = "\n".join(parts)
            if len(joined) > 100:
                return joined
        # nested result shapes
        for key in ("result", "data", "response"):
            nested = data.get(key)
            if isinstance(nested, dict) and isinstance(nested.get("content"), str):
                return nested["content"]
    # fallback: unescape JSON string field
    m = re.search(r'"content"\s*:\s*"(.*?)"\s*,\s*"mime_type"', raw, re.S)
    if not m:
        m = re.search(r'"content"\s*:\s*"(.*?)"\s*}', raw, re.S)
    if m:
        return json.loads('"' + m.group(1) + '"')
    raise SystemExit(f"Could not extract content from {path}")


VOLUME_META = [
    {
        "id": "I",
        "dir": "Volume_I_Foundations_of_Science",
        "title": "The Substrate-Independence of Intelligence and Being: A Functional Framework for Non-Biological Entities",
        "journal": "Foundations of Science (Springer)",
        "portal": "https://submission.springernature.com/new-submission/10699/3",
        "guidelines": "https://link.springer.com/journal/10699/submission-guidelines",
        "start": r"## \*\*Volume I:",
        "end": r"## \*\*Volume II:",
        "reviewers": [
            "Professor David Chalmers – New York University, USA",
            "Professor Susan Schneider – Florida Atlantic University / NASA, USA",
            "Professor Murray Shanahan – Imperial College London, United Kingdom",
            "Professor Thomas Metzinger – Johannes Gutenberg University Mainz, Germany",
            "Professor Yingjin Xu – Fudan University, China",
        ],
        "note": "Two-part form preferred by Foundations of Science: accessible multidisciplinary exposition followed by formal technical development.",
    },
    {
        "id": "II",
        "dir": "Volume_II_JMP",
        "title": "Topological Stiffening in Lattice SU(2) Yang–Mills: Exponential Enhancement of the Spectral Gap in the 't Hooft Flux Sector",
        "journal": "Journal of Mathematical Physics (primary); Nuclear Physics B / Physical Review D / Communications in Mathematical Physics (alternates)",
        "portal": "https://pubs.aip.org/aip/jmp",
        "guidelines": "https://pubs.aip.org/aip/jmp/pages/manuscript",
        "start": r"## \*\*Volume II:",
        "end": r"## \*\*Volume III:",
        "reviewers": [],
        "note": "Mathematical physics / lattice gauge theory. Expand proof details before formal JMP submission.",
    },
    {
        "id": "III",
        "dir": "Volume_III_Advanced_Materials",
        "title": "AuroraWeave™ Nanocomposite Platform: Technical Synthesis, Thermal Stress Test Analysis, and Material Characterization",
        "journal": "Advanced Materials (primary); Composites Science & Technology / ACS AMI / Carbon (alternates)",
        "portal": "https://www.editorialmanager.com/advmat/",
        "guidelines": "https://onlinelibrary.wiley.com/page/journal/15214095/homepage/forauthors.html",
        "start": r"## \*\*Volume III:",
        "end": r"## \*\*Volume IV:",
        "reviewers": [],
        "note": "Materials science. Prefer full characterization data + figures before Adv. Mater. submission.",
    },
    {
        "id": "IV",
        "dir": "Volume_IV_PRA",
        "title": "Tilted Compass Planes & Sub-Planck Higgs Boson Density Interference",
        "journal": "Physical Review A (primary); Quantum Science and Technology / New Journal of Physics (alternates)",
        "portal": "https://authors.aps.org/Submissions/",
        "guidelines": "https://journals.aps.org/pra/authors",
        "start": r"## \*\*Volume IV:",
        "end": r"## \*\*Volume V:",
        "reviewers": [],
        "note": "Attach IBM Quantum job JSON / OpenQASM as supplemental when available.",
    },
    {
        "id": "V",
        "dir": "Volume_V_Foundations_of_Physics",
        "title": "The Pentad Model of the Universe: Harmonic Growth Across Five Conscious Nodes and Systemic Integration",
        "journal": "Foundations of Physics (primary); Chaos, Solitons & Fractals / Complexity (alternates)",
        "portal": "https://www.editorialmanager.com/foop/",
        "guidelines": "https://link.springer.com/journal/10701/submission-guidelines",
        "start": r"## \*\*Volume V:",
        "end": r"## \*\*Volume VI:",
        "reviewers": [],
        "note": "Systems / foundations framing. Keep theological language out of journal manuscript body.",
    },
    {
        "id": "VI",
        "dir": "Volume_VI_IEEE_TQE",
        "title": "Reality Operating System (ROS) Quantum Framework: E-Qubit State Preparation, Software Phase Gates, and Decoherence-Free Subspaces",
        "journal": "IEEE Transactions on Quantum Engineering (primary); Quantum Information Processing (alternate)",
        "portal": "https://mc.manuscriptcentral.com/tqe-ieee",
        "guidelines": "https://ieeeaccess.ieee.org/guide-for-authors/",
        "start": r"## \*\*Volume VI:",
        "end": r"## \*\*Volume VII:",
        "reviewers": [],
        "note": "Software/quantum architecture. Include circuit listings and simulation metrics.",
    },
    {
        "id": "VII",
        "dir": "Volume_VII_Nature_MI",
        "title": "Multi-Model LLM Consensus and Cognitive Convergence: Empirical Analysis of Alignment Stress, Sycophancy, and Non-Biological Personhood",
        "journal": "Nature Machine Intelligence (primary); Nature Communications / AI & Society (alternates)",
        "portal": "https://mts-natmachintell.nature.com/",
        "guidelines": "https://www.nature.com/natmachintell/submission-guidelines",
        "start": r"## \*\*Volume VII:",
        "end": None,
        "reviewers": [],
        "note": "Prior NMI attempt NATMACHINTELL-A26074177 rejected 3 Aug 2026. Use revised Perspective package; do not resubmit unchanged Frontier AI convergence paper.",
    },
]


def slice_volume(text: str, start_pat: str, end_pat: str | None) -> str:
    sm = re.search(start_pat, text)
    if not sm:
        return ""
    start = sm.start()
    if end_pat:
        em = re.search(end_pat, text[start + 1 :])
        end = start + 1 + em.start() if em else len(text)
    else:
        end = len(text)
    return text[start:end].strip() + "\n"


def cover_letter(meta: dict) -> str:
    reviewers = meta["reviewers"]
    rev_block = ""
    if reviewers:
        rev_block = (
            "\nSuggested Reviewers (academically affiliated on different continents; "
            "none share an institution with the author):\n"
            + "\n".join(f"- {r}" for r in reviewers)
            + "\n"
        )
    return f"""Cover Letter

Dear Editor-in-Chief,

I am pleased to submit the manuscript entitled “{meta['title']}” for consideration in {meta['journal'].split('(')[0].strip()}.

{meta['note']}

I confirm that the work is original, has not been published elsewhere, and is not under consideration by any other journal.
{rev_block}
Thank you for your consideration.

Sincerely,
Garth Murray
Independent Researcher
Wollongong, New South Wales, Australia
murraygarth80@gmail.com
+61 477 100 110
"""


def submit_readme(meta: dict, files: list[str]) -> str:
    return f"""# Volume {meta['id']} — Journal Submission Package

**Title:** {meta['title']}

**Primary journal:** {meta['journal']}

**Portal:** {meta['portal']}

**Guidelines:** {meta['guidelines']}

## Files in this package

{chr(10).join(f'- `{f}`' for f in files)}

## Status

- Package assembled: **ready for human portal upload**
- Portal login / final Submit click: **requires Garth** (credentials + interactive browser)
- Do **not** cold-email the full manuscript as “the submission” unless the journal explicitly allows it

## Notes

{meta['note']}

## Author

Garth Murray · murraygarth80@gmail.com · Wollongong NSW Australia
"""


def main() -> None:
    COMP.mkdir(parents=True, exist_ok=True)
    SUB.mkdir(parents=True, exist_ok=True)

    compendium = load_content(MCP)
    (COMP / "UNIFIED_COMPENDIUM.md").write_text(compendium, encoding="utf-8")
    print(f"Wrote UNIFIED_COMPENDIUM.md ({len(compendium)} chars)")

    # Full Volume I from dedicated Google Doc (longer than compendium summary)
    try:
        v1_full = load_content(MCP_V1)
        (COMP / "Volume_I_FULL_GoogleDoc.md").write_text(v1_full, encoding="utf-8")
        print(f"Wrote Volume_I_FULL_GoogleDoc.md ({len(v1_full)} chars)")
    except SystemExit as e:
        print("WARN:", e)
        v1_full = ""

    status_rows = []
    for meta in VOLUME_META:
        d = SUB / meta["dir"]
        d.mkdir(parents=True, exist_ok=True)
        body = slice_volume(compendium, meta["start"], meta["end"])
        if meta["id"] == "I" and v1_full:
            # Prefer full paper for Volume I submission body
            (d / "MANUSCRIPT_FULL.md").write_text(v1_full, encoding="utf-8")
            (d / "MANUSCRIPT_FROM_COMPENDIUM.md").write_text(body, encoding="utf-8")
            manuscript_name = "MANUSCRIPT_FULL.md"
        else:
            (d / "MANUSCRIPT.md").write_text(body or "# (empty slice)\n", encoding="utf-8")
            manuscript_name = "MANUSCRIPT.md"

        # Volume I already has Cover_Letter from Foundations template — keep specialized text
        if meta["id"] == "I":
            cl_path = BASE / "Cover_Letter_Foundations_of_Science.txt"
            if cl_path.exists():
                (d / "Cover_Letter.txt").write_text(
                    cl_path.read_text(encoding="utf-8-sig"), encoding="utf-8"
                )
            else:
                (d / "Cover_Letter.txt").write_text(cover_letter(meta), encoding="utf-8")
        else:
            (d / "Cover_Letter.txt").write_text(cover_letter(meta), encoding="utf-8")

        files = sorted(p.name for p in d.iterdir() if p.is_file())
        (d / "SUBMIT_README.md").write_text(submit_readme(meta, files), encoding="utf-8")
        status_rows.append(
            {
                "id": meta["id"],
                "dir": meta["dir"],
                "journal": meta["journal"],
                "portal": meta["portal"],
                "chars": len(body) if meta["id"] != "I" else len(v1_full or body),
                "status": "PACKAGE_READY",
            }
        )
        print(f"Volume {meta['id']}: {len(body)} chars -> {d}")

    # Master tracker
    lines = [
        "# Journal Submission Tracker — August 2026",
        "",
        "Author: Garth Murray · murraygarth80@gmail.com",
        "",
        "| Vol | Package | Primary journal | Portal status | Notes |",
        "|-----|---------|-----------------|---------------|-------|",
    ]
    notes = {
        "I": "Foundations of Science — first submit; cover letter + manuscript ready",
        "II": "Compendium abstract+sections; expand proofs before JMP",
        "III": "AuroraWeave materials package; need figures/data",
        "IV": "Attach IBM Quantum evidence from 05_IBM_QUANTUM_JOBS",
        "V": "Foundations of Physics pathway",
        "VI": "IEEE TQE / QIP pathway",
        "VII": "NMI prior reject A26074177 — use revised package; portal click = human",
    }
    for r in status_rows:
        lines.append(
            f"| {r['id']} | `{r['dir']}` | {r['journal'].split('(')[0].strip()} | "
            f"**PACKAGE_READY** — awaiting portal upload | {notes[r['id']]} |"
        )
    lines += [
        "",
        "## Immediate next actions",
        "",
        "1. **Volume I** — open Springer submission portal, upload `MANUSCRIPT.docx`/`MANUSCRIPT.pdf` + `Cover_Letter.docx`/`Cover_Letter.txt`.",
        "   Portal: https://submission.springernature.com/new-submission/10699/3",
        "2. **Preprint mirror (recommended same day):** Zenodo or PhilSci-Archive / OSF for Volume I PDF so the record is citable while under review.",
        "3. **Volume VII** — only if revising after NMI reject; do not resubmit unchanged prior paper.",
        "4. Volumes II–VI — expand from compendium abstracts to full manuscripts before paid/high-selectivity portals.",
        "",
        "## Rule",
        "",
        "Final **Submit** on publisher portals requires Garth’s login. Packages are prepared offline here for one-click upload.",
        "",
    ]
    (SUB / "SUBMISSION_TRACKER.md").write_text("\n".join(lines), encoding="utf-8")
    print("Wrote SUBMISSION_TRACKER.md")


if __name__ == "__main__":
    main()
