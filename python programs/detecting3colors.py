import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV

    lower_blue = np.array([110,0,0])
    upper_blue = np.array([130,255,255])

    lower_green = np.array([50, 0, 0])
    upper_green = np.array([70, 255, 255])

    lower_red = np.array([0, 0, 0])
    upper_red = np.array([20, 255, 255])

    # Threshold the HSV image to get only blue colors
    maskb = cv2.inRange(hsv, lower_blue, upper_blue)
    maskg = cv2.inRange(hsv, lower_green, upper_green)
    maskr = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    resb = cv2.bitwise_and(frame,frame, mask= maskb)
    resg = cv2.bitwise_and(frame, frame, mask=maskg)
    resr = cv2.bitwise_and(frame, frame, mask=maskr)

    cv2.imshow('frame',frame)
    """cv2.imshow('maskb',maskb)
    cv2.imshow('maskg', maskg)
    cv2.imshow('maskr', maskr)"""

    cv2.imshow('resb',resb)
    cv2.imshow('resg', resg)
    cv2.imshow('resr', resr)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()