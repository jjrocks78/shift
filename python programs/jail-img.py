from cv2 import *

a=imread("/home/cocoslabs/Documents/download.jpeg",1)
imshow("img",a)
waitKey(0)
#print(a.shape)
(x,y,z)=a.shape

for i in range(0,x):
    for j in range(0,y):
        for k in range(0,z):
            if i%10==0 or j%10==0:
                a[i][j][k]=0

imshow("img1",a)
waitKey(0)