import urllib2
import cv2
import numpy as np

url='http://192.168.1.13/cam-lo.jpg'

while True:
	imgResp=urllib2.urlopen(url)
	imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
	img=cv2.imdecode(imgNp,-1)
	#img=cv2.line(img,(0,0),(100,100),(0,0,255),10)
	
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower_blue = np.array([90, 50, 50])
	upper_blue = np.array([130, 255, 255])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	#result = cv2.bitwise_and(img, img, mask=mask)
	
	cv2.imshow('test',img)
	if ord('q')==cv2.waitKey(10):
		exit(0)