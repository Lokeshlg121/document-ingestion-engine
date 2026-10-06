from document_ingestion.extraction.pdf.text import extract_text

def test_extract_text():
    pdf_path = "data/samples/normal_text_test.pdf"
    pages = extract_text(pdf_path)
    assert "PDF Text Extraction Test Document" in pages[0]
    assert "This is the second page" in pages[1]
    assert "Final test page" in pages[2]
