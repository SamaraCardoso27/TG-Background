import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img1.jpg',0)
edges = cv2.Canny(img,100,200)

teste = cv2.imwrite('canny.jpg',edges)
