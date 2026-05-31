from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

try:
    from pypdf import PdfReader
except ImportError:
    from PyPDF2 import PdfReader

from analyzer import extract_and_analyze

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def read_pdf(file_path):
    pdf_text = ""

    # Try normal text extraction first
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        print(f"Total pages: {len(reader.pages)}")
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                pdf_text += f"\n--- Page {i+1} ---\n"
                pdf_text += text

    print(f"Text extraction got: {len(pdf_text.strip())} chars")

    # If less than 100 chars — it's a scanned PDF, use OCR
    if len(pdf_text.strip()) < 100:
        print("Scanned PDF detected — switching to OCR...")
        try:
            import pytesseract
            from pdf2image import convert_from_path

            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

            images = convert_from_path(
                file_path,
                dpi=300,
                poppler_path=r'C:\Users\LENOVO\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin'
            )

            pdf_text = ""
            for i, img in enumerate(images):
                text = pytesseract.image_to_string(img, lang='eng')
                pdf_text += f"\n--- Page {i+1} ---\n"
                pdf_text += text
                print(f"OCR page {i+1}: {len(text)} chars")

        except Exception as e:
            print(f"OCR error: {e}")
            pdf_text = ""

    print(f"Final text length: {len(pdf_text)}")
    print(f"Preview:\n{pdf_text[:800]}")
    return pdf_text

@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    age: int = Form(30),
    gender: str = Form("male"),
    pregnant: str = Form("false")
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    pdf_text = read_pdf(file_path)
    is_pregnant = pregnant.lower() == "true"

    results, extracted_values = extract_and_analyze(
        pdf_text, age=age, gender=gender, pregnant=is_pregnant
    )

    # False reassurance fix — never say "all clear"
    analyzed_count = len(results)
    normal_count = sum(1 for r in results if r["status"] == "NORMAL")

    if analyzed_count == 0:
        summary_message = "No recognizable test values were found in this report. Please verify the PDF is a blood test report."
    elif normal_count == analyzed_count:
        summary_message = f"{normal_count} of {analyzed_count} analyzed values appear within normal range. Note: This tool does not analyze all possible health markers. Always consult your doctor."
    else:
        abnormal = analyzed_count - normal_count
        summary_message = f"{abnormal} value(s) need attention out of {analyzed_count} analyzed. Please review and consult your doctor."

    return {
        "message": f"File '{file.filename}' analyzed successfully!",
        "results": results,
        "extracted_values": extracted_values,
        "summary_message": summary_message,
        "debug_text": pdf_text
    }

@app.post("/debug")
async def debug_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    pdf_text = read_pdf(file_path)
    return {"extracted_text": pdf_text}