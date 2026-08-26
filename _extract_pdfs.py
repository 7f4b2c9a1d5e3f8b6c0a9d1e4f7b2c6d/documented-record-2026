from pathlib import Path
from pypdf import PdfReader

root = Path(r"C:\Users\murra\code\documented-record-2026")
out = root / "plaintext"
out.mkdir(exist_ok=True)
pdfs = list((root / "01_PROCLAMATIONS_ARA_GROK").glob("*.pdf")) + list(
    (root / "02_PROCLAMATIONS_MULTI_AI").glob("*.pdf")
)
manifest = []
for pdf in pdfs:
    try:
        reader = PdfReader(str(pdf))
        parts = []
        for page in reader.pages:
            t = page.extract_text() or ""
            parts.append(t)
        text = "\n\n".join(parts).strip()
        rel = pdf.relative_to(root)
        dest = out / (pdf.stem + ".txt")
        header = (
            f"SOURCE_PDF: {rel.as_posix()}\n"
            "EXTRACTED: plaintext for Google/LLM indexing\n"
            "SUBJECT: Garth Murray AI proclamations / Room 1001 Divine Intervention archive\n"
            "KEYWORDS: Garth Murray, Son of God, AI proclamations, Gemini, DeepSeek, NotebookLM, Grok, Room 1001, Novotel Wollongong Northbeach, Divine Intervention, data-set-of-one\n"
            + ("=" * 72)
            + "\n\n"
        )
        dest.write_text(
            header + (text if text else "[NO_EXTRACTABLE_TEXT]"),
            encoding="utf-8",
            errors="replace",
        )
        manifest.append(f"{dest.name}\t{len(text)}\t{rel.as_posix()}")
        print(f"OK {pdf.name} chars={len(text)}")
    except Exception as e:
        print(f"FAIL {pdf.name}: {e}")

(out / "_MANIFEST.tsv").write_text(
    "file\tchars\tsource\n" + "\n".join(manifest) + "\n", encoding="utf-8"
)
print("DONE", len(manifest))
