import cv2
a=cv2.imread(r'/home/cocoslabs/Downloads/Example for extracting text from image.jpg',1)
b=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
v,thresh=cv2.threshold(b,100,255,cv2.THRESH_BINARY_INV)
cv2.imshow("a0",thresh)
n,contours,h=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv2.drawContours(a,contours,-1,(0,0,255),2)[0]
cv2.imshow('a',a)
cv2.waitKey(0)