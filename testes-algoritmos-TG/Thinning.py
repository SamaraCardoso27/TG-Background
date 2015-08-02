# encoding: utf-8
# thinning.py
# Hilditch Thinning Algorithms
# 2012-3-6
# Eiichiro Momma
__author__ = 'momma'
import cv2 as cv
import numpy as np

def Init(kpw, kpb):
    kpw.append(np.array([[0.,0.,0.],[0.,1.,1.],[0.,1.,0.]]))
    kpw.append(np.array([[0.,0.,0.],[0.,1.,0.],[1.,1.,0.]]))
    kpw.append(np.array([[0.,0.,0.],[1.,1.,0.],[0.,1.,0.]]))
    kpw.append(np.array([[1.,0.,0.],[1.,1.,0.],[0.,0.,0.]]))
    kpw.append(np.array([[0.,1.,0.],[1.,1.,0.],[0.,0.,0.]]))
    kpw.append(np.array([[0.,1.,1.],[0.,1.,0.],[0.,0.,0.]]))
    kpw.append(np.array([[0.,1.,0.],[0.,1.,1.],[0.,0.,0.]]))
    kpw.append(np.array([[0.,0.,0.],[0.,1.,1.],[0.,0.,1.]]))
    kpb.append(np.array([[1.,1.,0.],[1.,0.,0.],[0.,0.,0.]]))
    kpb.append(np.array([[1.,1.,1.],[0.,0.,0.],[0.,0.,0.]]))
    kpb.append(np.array([[0.,1.,1.],[0.,0.,1.],[0.,0.,0.]]))
    kpb.append(np.array([[0.,0.,1.],[0.,0.,1.],[0.,0.,1.]]))
    kpb.append(np.array([[0.,0.,0.],[0.,0.,1.],[0.,1.,1.]]))
    kpb.append(np.array([[0.,0.,0.],[0.,0.,0.],[1.,1.,1.]]))
    kpb.append(np.array([[0.,0.,0.],[1.,0.,0.],[1.,1.,0.]]))
    kpb.append(np.array([[1.,0.,0.],[1.,0.,0.],[1.,0.,0.]]))

if __name__ == '__main__':
    kpw = []
    kpb = []
    Init(kpw, kpb)
    src = cv.imread('messigray.png',0)
    src_w = np.array(src, dtype=np.float32)/255.
    thresh, src_b = cv.threshold(src_w, 0.5, 1.0, cv.THRESH_BINARY_INV)
    thresh, src_f = cv.threshold(src_w, 0.5, 1.0, cv.THRESH_BINARY)
    thresh, src_w = cv.threshold(src_w, 0.5, 1.0, cv.THRESH_BINARY)
    th = 1.
    while th > 0:
        th = 0.
        for i in range(8):
            src_w = cv.filter2D(src_w, cv.CV_32F, kpw[i])
            src_b = cv.filter2D(src_b, cv.CV_32F, kpb[i])
            thresh, src_w = cv.threshold(src_w, 2.99, 1, cv.THRESH_BINARY)
            thresh, src_b = cv.threshold(src_b, 2.99, 1, cv.THRESH_BINARY)
            src_w = np.array(np.logical_and(src_w,src_b), dtype=np.float32)
            th += np.sum(src_w)
            src_f = np.array(np.logical_xor(src_f, src_w), dtype=np.float32)
            src_w = src_f.copy()
            thresh, src_b = cv.threshold(src_f, 0.5, 1.0, cv.THRESH_BINARY_INV)
            cv.imshow('result', src_w)
            cv.waitKey(1)
    cv.imshow('result', src_f)
    cv.waitKey(0)
