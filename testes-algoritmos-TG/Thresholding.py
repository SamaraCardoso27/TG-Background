import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('img1.jpg',0)
img = cv2.medianBlur(img,5)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
 
bla = cv2.imwrite('bla.jpg',th3) 

