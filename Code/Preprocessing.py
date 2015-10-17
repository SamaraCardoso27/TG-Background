import cv2
import numpy as np
from skimage import morphology
import cPickle
from matplotlib import pyplot as plt
import hashlib
import string
import random
from pysimplesoap.client import SoapClient


def improveImage(wImage):
    img = cv2.imread(wImage)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
    cv2.imwrite('improveImage-1.jpg',gray)
    #print 'gray'
    return gray


def skeletonization(wGray):
    image = wGray
    size = np.size(image)
    skeletonization_img = np.zeros(image.shape,np.uint8)
     
    ret,image = cv2.threshold(image,127,255,0)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    done = False
     
    while(not done):
        eroded = cv2.erode(image,element)
        temp = cv2.dilate(eroded,element)
        temp = cv2.subtract(image,temp)
        skeletonization_img = cv2.bitwise_or(skeletonization_img,temp)
        image = eroded.copy()
     
        zeros = size - cv2.countNonZero(image)
        if zeros==size:
            done = True
    cv2.imwrite('skeletonization-1.jpg',skeletonization_img)
    #print('fim skeletonization-1')
    return skeletonization_img
    

def createKeyPoints(wImage):
    sift = cv2.SIFT(100)
    kp = sift.detect(wImage,None)
    keyPoints=cv2.drawKeypoints(wImage,kp)
    cv2.imwrite('createKeyPoints-1.jpg',keyPoints)
    #print('Saved Image-createKeyPoints-1')
    return keyPoints



    
def encryptFingerprint(keyPoints):
    d=cv2.FeatureDetector_create("SIFT")
    kp=d.detect(keyPoints)
    key = []
    insert_key = []
    keypoint = ''
    
    for i in kp:
        keypoint = str(i.pt)
        key.append(keypoint)
    
    len_key = len(key)
    for i in range(len_key):
        insert_key.append(hashlib.md5(key[i]).hexdigest())
    return (','.join(str(e) for e in insert_key))


def webservice(keypoint):
    client = SoapClient(wsdl="http://127.0.0.1:8000/TG/webservice/call/soap?WSDL")
    
    response = client.getKeyPointPerson(auth= '0DDEE29FAA57CF9DBEE480986E7B0686',
                                   person_data={'keypoints':keypoint})
    try:
        result = response
    except SoapFault as e:
        result = e
    return dict(xml_request=client.xml_request, 
                xml_response=client.xml_response,result=result)
  


  
def create_name(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def teste():
    return 'passou aqui'
