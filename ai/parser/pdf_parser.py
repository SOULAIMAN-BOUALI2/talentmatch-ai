import fitz
# le but de transformer pdf vers text

def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:

        text += page.get_text()

    return text