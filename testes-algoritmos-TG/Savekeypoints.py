import cv2
import cPickle

im=cv2.imread("sift_keypoints.jpg")
gr=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
d=cv2.FeatureDetector_create("SIFT")
kp=d.detect(gr)

index = []
for point in kp:
    temp = (point.pt, point.size, point.angle, point.response, point.octave, 
        point.class_id) 
    index.append(temp)

# Dump the keypoints
f = open("keypoints.txt", "w")
f.write(cPickle.dumps(index))
f.close()
