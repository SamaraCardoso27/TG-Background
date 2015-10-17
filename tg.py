import shutil
import os
import sys


system = sys.platform
if system == 'linux2':
    os.mkdir('/home/fingerprint')
    arq = open("teste.txt", "w")
    arq.write('Samara')
    arq.close()
    shutil.move('teste.txt','/home/fingerprint')
