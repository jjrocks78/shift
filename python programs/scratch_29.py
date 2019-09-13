import cv2
import numpy as np
from skimage import restoration,color
from skimage.util import random_noise
from scipy.signal import convolve2d as conv2
kernelgauss33= np.array([[0.0625,0.125,0.0625],[0.125,0.25,0.125],[0.0625,0.125,0.0625]])
kernelbox=np.array([[0.1111,0.1111,0.1111],[0.1111,0.1111,0.1111],[0.1111,0.1111,0.1111]])
kernelgauss55=(np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]]))/256
kernelcustom=np.array([[-1,-0.6,-1.4],[0.2,6,0.2],[-1.4,-0.6,-1]])
kernel=(np.array([[2,1,1,0,0],[1,1,2,1,0],[0,0,1,1,1],[0,0,0,1,2],[0,0,0,0,1]]))/16
image=cv2.imread("/home/cocoslabs/Downloads/1525eefe4cbeb0480e33bfcf1312b8f1.png",1)
img=np.asarray(image)
img=color.rgb2gray(img)
cv2.imshow("org",img)
# cv2.imwrite("/home/cocoslabs/Downloads/graynaruto1.png",image)
cv2.waitKey(0)

# image1 = conv2(img, kernel, 'same')
# cv2.imshow("blur",image1)
# cv2.waitKey(0)

image2=restoration.wiener(img,kernelgauss33,0.0000001)
cv2.imshow("deblur gauss33",image2)
image3=restoration.wiener(img,kernelbox,0.000001)
cv2.imshow("deblur box",image3)
image4=restoration.wiener(img,kernelgauss55,0.00001)
cv2.imshow("deblur gauss55",image4)
image5=restoration.wiener(img,kernelcustom,0.00001)
cv2.imshow("deblur custom",image5)
image6=restoration.wiener(img,kernel,0.9)
cv2.imshow("deblur motion",image6)
cv2.waitKey(0)

# noise_mean = 0;
# noise_var = 0.0001;
# estimated_nsr = 0
# gauss = random_noise(I, mode='gaussian', seed=None, clip=True)
# sp = random_noise(I, mode='s&p', seed=None, clip=True)
