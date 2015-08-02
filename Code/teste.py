import cv2
import numpy as np
from skimage import morphology
import cPickle
from matplotlib import pyplot as plt
import hashlib

def improveImage(wImage):
    img = cv2.imread(wImage)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
    cv2.imwrite('melhorar-imagem.jpg',gray)
    print('Saved Image')

improveImage('2015-07-13 22_28_38.909328.jpeg')


def skeletonization(wImage):
    img = cv2.imread(wImage)
    img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    size = np.size(img)
    skel = np.zeros(img.shape,np.uint8)
     
    ret,img = cv2.threshold(img,127,255,0)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    done = False
     
    while(not done):
        eroded = cv2.erode(img,element)
        temp = cv2.dilate(eroded,element)
        temp = cv2.subtract(img,temp)
        skel = cv2.bitwise_or(skel,temp)
        img = eroded.copy()
     
        zeros = size - cv2.countNonZero(img)
        if zeros==size:
            done = True
    cv2.imwrite('melhorando-skeletonization.jpg',skel)
    print('fim skeletonization')

skeletonization('melhorar-imagem.jpg')



def createKeyPoints(wImage):
    img = cv2.imread(wImage)
    sift = cv2.SIFT(200)
    kp = sift.detect(img,None)
    for i in kp:
        print('kp',i)
    print(len(str(i)))
        
    img=cv2.drawKeypoints(img,kp)
    
    cv2.imwrite('createKeyPoints.jpg',img)
    print('Saved Image-createKeyPoints')
    

createKeyPoints('melhorando-skeletonization.jpg')    


def saveKeyPoints(wImage):
    im=cv2.imread(wImage)
    gr=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    d=cv2.FeatureDetector_create("SIFT")
    kp=d.detect(gr)

    index = []
    for point in kp:
        temp = (point.pt, point.size, point.angle, point.response, point.octave, point.class_id) 
    index.append(temp)
    #print('index',index)
    #for i in index:
        #print('i',i)
        #print('hashlib',hashlib.md5(''.join(str(e) for e in i)).hexdigest())
    f = open("keypoints-teste.txt", "w")
    f.write(cPickle.dumps(index))
    print('Save KeyPoints')
    f.close()
saveKeyPoints('createKeyPoints.jpg')


def displayKeypoints(wImage):
    im=cv2.imread(wImage)
    index = cPickle.loads(open("keypoints-teste.txt").read())
    kp = []
    for point in index:
        temp = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1], _angle=point[2],  
                            _response=point[3], _octave=point[4], _class_id=point[5])
        print('point',point)
    kp.append(temp)
    imm=cv2.drawKeypoints(im, kp);
    cv2.imwrite('display_keypoints.jpg',imm)
    print('display keypoints')
    
 
displayKeypoints('createKeyPoints-1.jpg')












