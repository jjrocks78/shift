import cv2
import numpy as np
"""a=cv2.imread("/home/cocoslabs/Desktop/images_lpr/download.jpeg",1)
cv2.imshow("img",a,(120,30,30))
b=cv2.cvtColor(a,cv2.COLOR_BGR2HSV)
cv2.imshow("imgb",b)
cv2.waitKey(0)"""
green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)

red=np.uint8([[[0,0,255]]])
hsc_red= cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
print(hsc_red)

blue=np.uint8([[[255,0,0]]])
hsc_blue= cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
print(hsc_blue)