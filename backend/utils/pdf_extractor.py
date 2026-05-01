# utils.py
import fitz  # PyMuPDF
import re

def extract_clean_text(file_bytes: bytes) -> str:
    """Extracts text from PDF bytes and removes excessive whitespace."""
    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = "".join(page.get_text() for page in doc)
        
        # Clean up the text: replace multiple spaces/newlines with a single space
        clean_text = re.sub(r'\s+', ' ', text).strip()
        return clean_text
    except Exception as e:
        raise ValueError(f"Failed to parse PDF: {str(e)}")