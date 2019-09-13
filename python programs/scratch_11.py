# import the necessary packages
import imutils
import cv2
import random as rng
import numpy as np

image = cv2.imread(r'/home/cocoslabs/Downloads/Example for extracting text from image.jpg',1)
(h, w, d) = image.shape
#print("width={}, height={}, depth={}".format(w, h, d))
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#cv2.imshow("Image", image)

_,thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(cnts)
output = image.copy()

# loop over the contours
"""for c in cnts:
    # draw each contour on the output image with a 3px thick purple
    # outline, then display the output contours one at a time
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
    cv2.imshow("Contours", output)
    cv2.waitKey(100)
print(len(cnts))"""
contours_poly = [None] * len(contours)
boundRect = [None] * len(contours)
centers = [None] * len(contours)
radius = [None] * len(contours)
for i, c in enumerate(contours):
    contours_poly[i] = cv2.approxPolyDP(c, 3, True)
    boundRect[i] = cv2.boundingRect(contours_poly[i])
    centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])

drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), dtype=np.uint8)



for i in range(len(contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv2.drawContours(drawing, contours_poly, i, color)
        cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])),
          (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
        cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)

cv2.imshow('Contours', drawing)



x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
