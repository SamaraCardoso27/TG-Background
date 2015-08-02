import sqlite3
import hashlib
import cv2
import cPickle


conn = sqlite3.connect('TG.db')

c = conn.cursor()
c.execute('''CREATE TABLE person(
             name text,
             keypoint text,
             creation_date text
        );''')



def insert(name,keypoint,creation_date):
    print('name'+name)
    print('keypoint'+''.join(str(k) for k in keypoint))
    print('creation_date'+creation_date)
    d=cv2.FeatureDetector_create("SIFT")
    kp=d.detect(keypoint)
    key = []
    for point in kp:
        temp = (point.pt, point.size, point.angle, point.response, point.octave, point.class_id) 
    key.append(temp)
    keypoint = (cPickle.dumps(hashlib.md5(''.join(str(e) for e in key)).hexdigest()))
    c.execute("INSERT INTO fingerprint (name,keypoint,creation_date) VALUES ("+name+","+keypoint+","+creation_date+");")
    return 'Inserido com sucesso'
    
def search(keypoint):
    for row in c.execute('SELECT * FROM fingerprint WHERE keypoint = '+str(keypoint)):
        if (row != ''):
            return True
        return False
    