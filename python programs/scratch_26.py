import cv2
import numpy as np
from skimage import restoration,color
from scipy.signal import convolve2d as conv2
from scipy.signal import convolve as conv
image=cv2.imread("/home/cocoslabs/Downloads/images.png",1)
cv2.imshow("original image",image)
cv2.waitKey(0)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",gray)
cv2.waitKey(0)

bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("black and white image",bw)
cv2.waitKey(0)

bwi = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("black and white inverted image",bwi)
cv2.waitKey(0)

blurImg = cv2.blur(image, (5, 5))
cv2.imshow('blurred image', blurImg)
cv2.waitKey(0)

blurImg1=cv2.cvtColor(blurImg,cv2.COLOR_BGR2GRAY)
cv2.imshow('blurred1 image', blurImg1)
cv2.waitKey(0)

img=np.asarray(image)
img=color.rgb2gray(img)
psf = np.ones((5, 5)) / 25
print(img.ndim, psf.ndim)
image1 = conv2(img, psf, 'same')
image1 += 0.2 * image1.std() * np.random.standard_normal(image1.shape)

deconvolved, _ = restoration.unsupervised_wiener(image1, psf)
cv2.imshow('deblurred image', deconvolved)
cv2.waitKey(0)
#
# img=np.asarray(image)
# # img=color.rgb2gray(img)
# psf = np.ones((5,5,3)) / 75
# print(img.ndim, psf.ndim)
# image1 = conv(img, psf, 'same')
# image1 += 0.2 * image1.std() * np.random.standard_normal(image1.shape)
#
# deconvolved1, _ = restoration.unsupervised_wiener(image1, psf)
# cv2.imshow('deblurred1 image', deconvolved1)
# cv2.waitKey(0)
# print(0.5 * image1.std() * np.random.standard_normal(image1.shape))


