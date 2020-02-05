import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

A=Image.open('C:/Users/eh3g/Documents/GitHub/Calendar_Events/test_image/test1.jpg')
text=pytesseract.image_to_string(A)
print(text)
