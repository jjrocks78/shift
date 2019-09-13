from os import listdir
from os.path import isfile, join
import numpy,os
import random
import cv2
from skimage.exposure import rescale_intensity
from skimage.segmentation import slic
from skimage.util import img_as_float
from skimage import io
import numpy as np
#RESIZE
def resize_image(image,w,h):
    print("1")
    image=cv2.resize(image,(w,h))
    cv2.imwrite(Folder_name+"/Resize-"+str(w)+"*"+str(h)+Extension, image)

#crop
def crop_image(image,y1,y2,x1,x2):
    print("2")
    image=image[y1:y2,x1:x2]
    cv2.imwrite(Folder_name+"/Crop-"+str(x1)+str(x2)+"*"+str(y1)+str(y2)+Extension, image)

def padding_image(image,topBorder,bottomBorder,leftBorder,rightBorder,color_of_border=[0,0,0]):
    print("3")
    image = cv2.copyMakeBorder(image,topBorder,bottomBorder,leftBorder,
        rightBorder,cv2.BORDER_CONSTANT,value=color_of_border)
    cv2.imwrite(Folder_name + "/padd-" + str(topBorder) + str(bottomBorder) + "*" + str(leftBorder) + str(rightBorder) + Extension, image)

def flip_image(image,dir):
    print("4")
    image = cv2.flip(image, dir)
    cv2.imwrite(Folder_name + "/flip-" + str(dir)+Extension, image)

def superpixel_image(image,segments):
    seg=segments

    def segment_colorfulness(image, mask):
        # split the image into its respective RGB components, then mask
        # each of the individual RGB channels so we can compute
        # statistics only for the masked region
        (B, G, R) = cv2.split(image.astype("float"))
        R = np.ma.masked_array(R, mask=mask)
        G = np.ma.masked_array(B, mask=mask)
        B = np.ma.masked_array(B, mask=mask)

        # compute rg = R - G
        rg = np.absolute(R - G)

        # compute yb = 0.5 * (R + G) - B
        yb = np.absolute(0.5 * (R + G) - B)

        # compute the mean and standard deviation of both `rg` and `yb`,
        # then combine them
        stdRoot = np.sqrt((rg.std() ** 2) + (yb.std() ** 2))
        meanRoot = np.sqrt((rg.mean() ** 2) + (yb.mean() ** 2))

        # derive the "colorfulness" metric and return it
        return stdRoot + (0.3 * meanRoot)

    orig = cv2.imread(image)
    vis = np.zeros(orig.shape[:2], dtype="float")

    # load the image and apply SLIC superpixel segmentation to it via
    # scikit-image
    image = io.imread(image)
    segments = slic(img_as_float(image), n_segments=segments,
                    slic_zero=True)
    for v in np.unique(segments):
        # construct a mask for the segment so we can compute image
        # statistics for *only* the masked region
        mask = np.ones(image.shape[:2])
        mask[segments == v] = 0

        # compute the superpixel colorfulness, then update the
        # visualization array
        C = segment_colorfulness(orig, mask)
        vis[segments == v] = C
    # scale the visualization image from an unrestricted floating point
    # to unsigned 8-bit integer array so we can use it with OpenCV and
    # display it to our screen
    vis = rescale_intensity(vis, out_range=(0, 255)).astype("uint8")

    # overlay the superpixel colorfulness visualization on the original
    # image
    alpha = 0.6
    overlay = np.dstack([vis] * 3)
    output = orig.copy()
    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
    # cv2.imshow("Visualization", vis)
    cv2.imwrite(Folder_name + "/superpixels-" + str(seg) + Extension, output)

def invert_image(image,channel):
    # image=cv2.bitwise_not(image)
    print("5")
    image=(channel-image)
    cv2.imwrite(Folder_name + "/invert-"+str(channel)+Extension, image)

def add_light(image, gamma=1.0):
    print("6")
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    image=cv2.LUT(image, table)
    if gamma>=1:
        cv2.imwrite(Folder_name + "/light-"+str(gamma)+Extension, image)
    else:
        cv2.imwrite(Folder_name + "/dark-" + str(gamma) + Extension, image)

def add_light_color(image, color, gamma=1.0):
    print("7")
    invGamma = 1.0 / gamma
    image = (color - image)
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    image=cv2.LUT(image, table)
    if gamma>=1:
        cv2.imwrite(Folder_name + "/light_color-"+str(gamma)+Extension, image)
    else:
        cv2.imwrite(Folder_name + "/dark_color" + str(gamma) + Extension, image)

def saturation_image(image,saturation):
    print("8")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    v = image[:, :, 2]
    v = np.where(v <= 255 - saturation, v + saturation, 255)
    image[:, :, 2] = v

    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    cv2.imwrite(Folder_name + "/saturation-" + str(saturation) + Extension, image)

def hue_image(image,saturation):
    print("9")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    v = image[:, :, 2]
    v = np.where(v <= 255 + saturation, v - saturation, 255)
    image[:, :, 2] = v

    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    cv2.imwrite(Folder_name + "/hue-" + str(saturation) + Extension, image)


mypath="/home/cocoslabs/Desktop/New_jj/"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
os.mkdir("/home/cocoslabs/Desktop/New")
for n in range(0, len(onlyfiles)):
    images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
    os.mkdir("/home/cocoslabs/Desktop/New/"+"img%d/"%n)
    path1=os.getcwd()
    Folder_name = "/home/cocoslabs/Desktop/New/"+"img%d"%n
    Extension = ".jpg"

    image = images[n]
    resize_image(image, 450, 400)

    crop_image(image, 100, 400, 0, 350)  # (y1,y2,x1,x2)(bottom,top,left,right)
    crop_image(image, 100, 400, 100, 450)  # (y1,y2,x1,x2)(bottom,top,left,right)
    crop_image(image, 0, 300, 0, 350)  # (y1,y2,x1,x2)(bottom,top,left,right)
    crop_image(image, 0, 300, 100, 450)  # (y1,y2,x1,x2)(bottom,top,left,right)
    crop_image(image, 100, 300, 100, 350)  # (y1,y2,x1,x2)(bottom,top,left,right)

    padding_image(image, 100, 0, 0, 0)  # (y1,y2,x1,x2)(bottom,top,left,right)
    padding_image(image, 0, 100, 0, 0)  # (y1,y2,x1,x2)(bottom,top,left,right)
    padding_image(image, 0, 0, 100, 0)  # (y1,y2,x1,x2)(bottom,top,left,right)
    padding_image(image, 0, 0, 0, 100)  # (y1,y2,x1,x2)(bottom,top,left,right)
    padding_image(image, 100, 100, 100, 100)  # (y1,y2,x1,x2)(bottom,top,left,right)

    flip_image(image, 0)  # horizontal
    flip_image(image, 1)  # vertical
    flip_image(image, -1)  # both

    """superpixel_image(image, 100)
    superpixel_image(image, 50)
    superpixel_image(image, 25)
    superpixel_image(image, 75)
    superpixel_image(image, 200)"""

    invert_image(image, 255)
    invert_image(image, 200)
    invert_image(image, 150)
    invert_image(image, 100)
    invert_image(image, 50)

    add_light(image, 1.5)
    add_light(image, 2.0)
    add_light(image, 2.5)
    add_light(image, 3.0)
    add_light(image, 4.0)
    add_light(image, 5.0)
    add_light(image, 0.7)
    add_light(image, 0.4)
    add_light(image, 0.3)
    add_light(image, 0.1)

    add_light_color(image, 255, 1.5)
    add_light_color(image, 200, 2.0)
    add_light_color(image, 150, 2.5)
    add_light_color(image, 100, 3.0)
    add_light_color(image, 50, 4.0)
    add_light_color(image, 255, 0.7)
    add_light_color(image, 150, 0.3)
    add_light_color(image, 100, 0.1)

    saturation_image(image, 50)
    saturation_image(image, 100)
    saturation_image(image, 150)
    saturation_image(image, 200)

    hue_image(image, 50)
    hue_image(image, 100)
    hue_image(image, 150)
    hue_image(image, 200)