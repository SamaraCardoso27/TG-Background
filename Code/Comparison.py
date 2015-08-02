import cv2
import numpy as np
from skimage import morphology
import cPickle
from matplotlib import pyplot as plt

def drawMatchesKNN(img1, kp1, img2, kp2, matches):
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]
    out = np.zeros((max([rows1,rows2]),cols1+cols2,3), dtype='uint8')
    out[:rows1,:cols1,:] = np.dstack([img1, img1, img1])
    out[:rows2,cols1:cols1+cols2,:] = np.dstack([img2, img2, img2])
    for (img1_idx,mat) in enumerate(matches):
        (x1,y1) = kp1[img1_idx].pt
        for mat2 in mat:
            img2_idx = mat2.trainIdx
            (x2,y2) = kp2[img2_idx].pt
            cv2.circle(out, (int(x1),int(y1)), 4, (255, 0, 0), 1)
            cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (255, 0, 0), 1)
            cv2.line(out, (int(x1),int(y1)), (int(x2)+cols1,int(y2)), (255, 0, 0), 1)
    
    cv2.imshow('Matched Features', out)
    cv2.imwrite('comparacao.jpg',out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return out 


def comparison_fingerprints():
    img1 = cv2.imread('createKeyPoints-1.jpg',0)
    img2 = cv2.imread('createKeyPoints-1.jpg',0) 
    sift = cv2.SIFT(100) 
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)  
    flann = cv2.FlannBasedMatcher(index_params,search_params)  
    matches = flann.knnMatch(des1,des2,k=2)
    matchesMask = [[0,0] for i in xrange(len(matches))]
    
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            matchesMask[i]=[1,0]
    
    draw_params = dict(matchColor = (0,255,0),
                       singlePointColor = (255,0,0),
                       matchesMask = matchesMask,
                       flags = 0)
    
    img3 = drawMatchesKNN(img1,kp1,img2,kp2,matches)
    
    
    
comparison_fingerprints()
