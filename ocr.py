import Image
from tesseract import image_to_string

print(image_to_string(Image.open('E:\\aa.png')))
print(image_to_string(Image.open('E:\\aa.png'), lang='eng'))
