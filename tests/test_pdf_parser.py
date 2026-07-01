from ai.parser.pdf_parser import extract_text

def test_pdf_parser():

    text = extract_text("storage/cvs/test.pdf")

    assert text is not None
    assert len(text) > 0