import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('teste.jpg',0)

ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)


images = [thresh5]

for i in xrange(6):
    plt.imshow(images[i])


plt.show()
