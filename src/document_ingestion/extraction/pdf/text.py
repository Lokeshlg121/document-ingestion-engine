import pymupdf
from pathlib import Path


def extract_text(pdf_source:str | Path | bytes) -> list[str]:
  if isinstance(pdf_source,bytes):
    document = pymupdf.open(
      stream= pdf_source,
      filetype= "pdf"
    )
  else: 
    pdf_path = Path(pdf_source)
    if not pdf_path.is_file():
      raise FileNotFoundError("File not Found")
    document = pymupdf.open(pdf_source)

#   print("doccc",document[0])  
  pages = []
  for page in document:
    page_text = page.get_text()
    print("Page number:", page.number + 1)
    print("Extracted text:", page_text)
    pages.append(page_text)

    
  return pages
  