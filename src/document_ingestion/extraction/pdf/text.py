import pymupdf
from pathlib import Path



def extract_text(pdf_path:str) -> list[str]:
    path = Path(pdf_path)
    if not path.is_file():
        raise FileNotFoundError("File not found: {pdf_path}")
    document = pymupdf.open(pdf_path)
    pages = []
    for page in document:
        text = page.get_text()
        pages.append(text)

    document.close()
    return pages
