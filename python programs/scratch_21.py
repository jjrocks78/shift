import cv2

TEXT_TOP = 680
TEXT_BOTTOM = 740
TEXT_LEFT = 280
TEXT_RIGHT = 1080

img = cv2.imread ('/home/cocoslabs/Downloads/4l3bn.jpg')

cropped = img [TEXT_TOP: TEXT_BOTTOM, TEXT_LEFT: TEXT_RIGHT]

white_region = cv2.inRange (cropped, (200, 200, 200), (255, 255, 255))

cv2.imshow ('white_region', white_region)
cv2.waitKey (10000)