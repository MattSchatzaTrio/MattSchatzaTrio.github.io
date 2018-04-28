#messing

import cv2
import numpy as np
from matplotlib import pyplot as plt


im_gray = cv2.imread('./images/insta.png',cv2.IMREAD_UNCHANGED)

#insta
height, width,stuff = im_gray.shape
crop_img = im_gray[1:height-1,int(width/2)+45:int(width)-1]
#(thresh, im_bw) = cv2.threshold(crop_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#thresh = 20
#im_bw = cv2.threshold(crop_img, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('./images/color_insta.png',crop_img)

#fb
#(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#thresh = 170
#im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
#cv2.imwrite('bw_fb.png',im_bw)
