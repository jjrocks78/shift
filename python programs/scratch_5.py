import cv2
imS = cv2.resize(warped, (1350, 1150))
cv2.imshow("output",imS)
cv2.imwrite('Output Image.PNG', imS)
cv2.waitKey(0)
from PIL import Image
import PIL.Image

from pytesseract import image_to_string
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'
output = pytesseract.image_to_string(PIL.Image.open('Output Image.PNG').convert("RGB"), lang='eng')
print output
import cv2

img = cv2.imread("input_image.png", 0)
ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
print "Threshold selected : ", ret
cv2.imwrite("./output_image.png", thresh)