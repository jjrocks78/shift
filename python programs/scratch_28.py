import cv2

a=cv2.imread("/home/cocoslabs/Downloads/images (1).jpeg",1)
b=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
thresh=cv2.threshold(b,127,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow("original",a)
cv2.waitKey(0)

mask=thresh.copy()
output = cv2.bitwise_and(a, b, mask=mask)
cv2.imshow("Output", output)
cv2.waitKey(0)