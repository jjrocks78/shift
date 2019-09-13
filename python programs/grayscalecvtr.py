import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh, blackAndWhiteImage = cv2.threshold(grayImage, 80, 255, cv2.THRESH_BINARY)

    cv2.imshow("b&w",blackAndWhiteImage)
    cv2.imshow("gray",grayImage)


    # Threshold the HSV image to get only blue colors


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()