import cv2
import imutils

a=cv2.imread('/home/cocoslabs/Documents/images.jpeg',1)
b=imutils.rotate_bound(a,90)

(h,w,d)=( b.shape)
b=imutils.resize(b,width=int(w*0.4))
cv2.imshow('img',b)
cv2.waitKey(0)
cv2.imwrite('/home/cocoslabs/Documents/image11.jpeg',b)

print(b.shape)
