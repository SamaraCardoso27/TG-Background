import cv2
import cPickle

im=cv2.imread("sift_keypoints.jpg")

index = cPickle.loads(open("keypoints.txt").read())

kp = []

for point in index:
    temp = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1], _angle=point[2], 
                            _response=point[3], _octave=point[4], _class_id=point[5]) 
    kp.append(temp)

# Draw the keypoints
imm=cv2.drawKeypoints(im, kp);
cv2.imwrite("key.jpg",imm)
