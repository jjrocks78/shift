# % Load image
# I = im2double(imread('image_src.png'));
# figure(1); imshow(I); title('Source image');
#
# % Blur image
# PSF = fspecial('disk', 15);
# Blurred = imfilter(I, PSF,'circular','conv' );
#
# % Add noise
# noise_mean = 0;
# noise_var = 0.00001;
# Blurred = imnoise(Blurred, 'gaussian', noise_mean, noise_var);
# figure(2); imshow(Blurred); title('Blurred image');
# estimated_nsr = noise_var / var(Blurred(:));
#
# % Restore image
# figure(3), imshow(deconvwnr(Blurred, PSF, estimated_nsr)), title('Wiener');
# figure(4); imshow(deconvreg(Blurred, PSF)); title('Regul');
# figure(5); imshow(deconvblind(Blurred, PSF, 100));
# title('Blind');
# figure(6); imshow(deconvlucy(Blurred, PSF, 100));
# title('Lucy');

# import cv2
# import numpy as np
# a=cv2.imread("/home/cocoslabs/Downloads/1525eefe4cbeb0480e33bfcf1312b8f1.png",1)
# image=cv2.blur(a,(10,10))
# cv2.imshow("blur",image)
# cv2.waitKey(0)
# print(image.shape)
# row,col,ch = image.shape
# s_vs_p = 0.5
# amount = 0.004
# out = np.copy(image)
# # Salt mode
# num_salt = np.ceil(amount * image.size * s_vs_p)
# coords = [np.random.randint(0, i - 1, int(num_salt))
#       for i in image.shape]
# out[coords] = 1
#
# # Pepper mode
# num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
# coords = [np.random.randint(0, i - 1, int(num_pepper))
#       for i in image.shape]
# out[coords] = 0
# cv2.imshow('nosiy',out)
# cv2.waitKey(0)

# import numpy as np
# import os
# import cv2
# def noisy(noise_typ,image):
#    if noise_typ == "gauss":
#       row,col,ch= image.shape
#       mean = 0
#       var = 0.1
#       sigma = var**0.5
#       gauss = np.random.normal(mean,sigma,(row,col,ch))
#       gauss = gauss.reshape(row,col,ch)
#       noisy = image + gauss
#       return noisy
#    elif noise_typ == "s&p":
#       row,col,ch = image.shape
#       s_vs_p = 0.5
#       amount = 0.004
#       out = np.copy(image)
#       # Salt mode
#       num_salt = np.ceil(amount * image.size * s_vs_p)
#       coords = [np.random.randint(0, i - 1, int(num_salt))
#               for i in image.shape]
#       out[coords] = 1
#
#       # Pepper mode
#       num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
#       coords = [np.random.randint(0, i - 1, int(num_pepper))
#               for i in image.shape]
#       out[coords] = 0
#       return out
#    elif noise_typ == "poisson":
#        vals = len(np.unique(image))
#        vals = 2 ** np.ceil(np.log2(vals))
#        noisy = np.random.poisson(image * vals) / float(vals)
#        return noisy
#    elif noise_typ =="speckle":
#        row,col,ch = image.shape
#        gauss = np.random.randn(row,col,ch)
#        gauss = gauss.reshape(row,col,ch)
#        noisy = image + image * gauss
#        return noisy
#
# a=cv2.imread("/home/cocoslabs/Downloads/1525eefe4cbeb0480e33bfcf1312b8f1.png",1)
# n=noisy("gauss",a)
# n1=noisy("s&p",a)
# n2=noisy("poisson",a)
# n3=noisy("speckle",a)
# cv2.imshow("a",a)
# cv2.imshow("gauss",n)
# cv2.imshow("s&p",n1)
# cv2.imshow("poisson",n2)
# cv2.imshow("speckle",n3)
# cv2.waitKey(0)




from skimage import color, data, restoration
import cv2
import numpy as np
from scipy import ndimage

img=cv2.imread("/home/cocoslabs/Downloads/1525eefe4cbeb0480e33bfcf1312b8f1.png",1)
im=np.asarray(img)
# print(im.shape)

# First a 1-D  Gaussian
t = np.linspace(-10, 10, 30)
bump = np.exp(-0.1*t**2)
bump /= np.trapz(bump) # normalize the integral to 1

# make a 2-D kernel out of it
kernel = bump[:, np.newaxis] * bump[np.newaxis, :]

blur=cv2.filter2D(img, -1, kernel)
cv2.imshow('blur',blur)
cv2.waitKey(0)
blur1=np.asarray(blur)
print(blur1.shape)
row,col,ch= blur.shape
mean = 0
var = 0.00001
sigma = var**0.5
gauss = np.random.normal(mean,sigma,(row,col,ch))
gauss = gauss.reshape(row,col,ch)
noisy = blur + gauss
cv2.imshow("noisy",noisy)
cv2.waitKey(0)

win_rows, win_cols = 5, 5
win_mean = ndimage.uniform_filter(blur1, (win_rows, win_cols,3))
win_sqr_mean = ndimage.uniform_filter(blur1**2, (win_rows, win_cols,3))
win_var = win_sqr_mean - win_mean**2
#estimated_var=var/win_var
# print(estimated_var)
deconvolved, _ = restoration.unsupervised_wiener(img, kernel)
cv2.imshow("wer",deconvolved)
cv2.waitKey(0)