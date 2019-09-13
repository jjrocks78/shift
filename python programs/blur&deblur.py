import cv2
import numpy as np
from skimage import restoration,color
from skimage.util import random_noise
from scipy.signal import convolve2d as conv2
kernel= (np.array([[2,1,1,0,0],[1,1,2,1,0],[0,0,1,1,1],[0,0,0,1,2],[0,0,0,0,1]]))/16
kernel2=np.array([[0,0,0],[0,1,0],[0,0,0]])
image=cv2.imread("/home/cocoslabs/Downloads/images.png",1)
img=np.asarray(image)
img=color.rgb2gray(img)
cv2.imshow("org",img)
# cv2.imwrite("/home/cocoslabs/Downloads/graynaruto1.png",image)
cv2.waitKey(0)

image1 = conv2(img, kernel, 'same')
cv2.imshow("blur",image1)
cv2.waitKey(0)

image2=restoration.wiener(image1,kernel,0.0001)
cv2.imshow("deblur",image2)
cv2.waitKey(0)

# noise_mean = 0;
# noise_var = 0.0001;
# estimated_nsr = 0
# gauss = random_noise(I, mode='gaussian', seed=None, clip=True)
# sp = random_noise(I, mode='s&p', seed=None, clip=True)
