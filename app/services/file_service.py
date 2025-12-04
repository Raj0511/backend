import io
from pypdf import PdfReader

async def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Synchronous PDF parsing wrapped in an async function.
    """
    pdf_stream = io.BytesIO(file_bytes)
    
    reader = PdfReader(pdf_stream)
    text = ""
    
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"
            
    return text