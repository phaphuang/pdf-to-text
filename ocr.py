import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

file_name = 'temp.jpg'
txtImg = Image.open(file_name)
text = pytesseract.image_to_string(txtImg)

print(text)
