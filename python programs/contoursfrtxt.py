# import the necessary packages
import imutils
import cv2
import random as rng
import numpy as np

image = cv2.imread(r'/home/cocoslabs/Downloads/Example for extracting text from image.jpg',1)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#cv2.imshow("Image", image)

_,thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(cnts)
output = image.copy()
output1=image.copy()
d=0

# loop over the contours
for c in contours:
    # draw each contour on the output image with a 3px thick purple
    # outline, then display the output contours one at a time
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Contours", output)
    cv2.waitKey(10)
cv2.putText(output,"that's it {} contours".format((len(contours))),(10,100),cv2.FONT_HERSHEY_COMPLEX,1.2,(0,0,0),2)
cv2.imshow("output",output)
cv2.waitKey(0)
print(len(contours))


"""
for c1 in contours:
    # draw each contour on the output image with a 3px thick purple
    # outline, then display the output contours one at a time
    (x1, y1), radius = cv2.minEnclosingCircle(c1)
    center = (int(x1), int(y1))
    radius = int(radius)
    cv2.circle(output1, center, radius, (0, 255, 0), 2)
    cv2.imshow("Contours", output)
    cv2.waitKey(100)
cv2.putText(output,"that's it {} contours".format((len(contours))),(10,100),cv2.FONT_HERSHEY_COMPLEX,1.2,(0,0,0),2)
cv2.imshow("output",output)
cv2.waitKey(0)
print(len(contours))


"""