from PIL import Image
import pytesseract
from parser.parser import extract_tests

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open("report.png")

text = pytesseract.image_to_string(img)

tests = extract_tests(text)

print(tests)