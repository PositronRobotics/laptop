import urllib2
import cv2
import numpy as np

url='http://192.168.1.13/cam-lo.jpg'

while True:
    imgResp=urllib2.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    # all the opencv processing is done here
    cv2.imshow('test',img)
    if ord('q')==cv2.waitKey(10):
        exit(0)