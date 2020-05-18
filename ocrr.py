from PIL import Image
import pytesseract

print(pytesseract.image_to_string(Image.open('E:\\aa.png')))
print(pytesseract.image_to_string(Image.open('E:\\aa.png'), lang='eng'))
