from PIL import Image
import pytesseract

i=Image.open('/home/cocoslabs/Downloads/Example for extracting text from image.jpg')

text= pytesseract.image_to_string(i,lang="english")

print(text)