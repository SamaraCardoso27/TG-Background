import cv2
import numpy as np
import hashlib
import cPickle
import re

f = open('keypoints-teste.txt')
points = ''
bla = []
for linha in f:
    points = points + (linha)
f.close()
#print(points)
for i in points[0]:
    m = re.search("\'\(\d+.\d+\, \d+.\d+\)\'",i)
    #bla.append(str(m.group(2)))
#print(bla)






img = cv2.imread('img1.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT(100)
kp = sift.detect(gray,None)

key = ''
for i in kp:
    key = key + str(i.pt)
#print(len(key))
#print(key)
#print(key)
#len_key = len(key)
#teste = []
#for i in range(len_key):
#    teste.append(hashlib.md5(key[i]).hexdigest())
#print(teste)
#f = open("keypoints-teste.txt", "w")
#f.write(cPickle.dumps(key))
#print('fim')



def comp(list1, list2):
    igual = ''
    for val in (list1):
        if val in list2:
            igual = igual + val
    percentual = (len(list2) * 100 / len(list1))
    if percentual >= 80:
        print('SIM')
    else:
        print('NAO')
comp(points[0],key)





