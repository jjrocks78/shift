# I = im2double(imread('IMG_REAL_motion_blur.PNG'));
# figure(1); imshow(I); title('Source image');
#
# %PSF
# PSF = fspecial('motion', 14, 0);
# noise_mean = 0;
# noise_var = 0.0001;
# estimated_nsr = noise_var / var(I(:));
#
# I = edgetaper(I, PSF);
# figure(2); imshow(deconvwnr(I, PSF, estimated_nsr)); title('Result')


from cv2 import *
import numpy as np
from scipy import ndimage

def im2double(im):
    min_val = np.min(im.ravel())
    max_val = np.max(im.ravel())
    out = (im.astype('float') - min_val) / (max_val - min_val)
    return out

img=im2double(imread('/home/cocoslabs/Downloads/9d8554c156e63a213797502e4d5b9075.png'))
a=np.asarray(img)
imshow("s",img)
waitKey(0)

size = 15

# generating the kernel
kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size

# applying the kernel to the input image
output = cv2.filter2D(img, -1, kernel_motion_blur)

imshow('Motion Blur', output)
waitKey(0)

noise_mean = 0;
noise_var = 0.0001;
estimated_nsr = noise_var /ndimage.variance(a)
print(estimated_nsr)

blur=blur(img,(10,10))
imshow("blur",blur)
waitKey(0)


