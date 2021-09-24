# Import essential libraries
import requests
import cv2
import numpy as np
import imutils
from cvzone.HandTrackingModule import HandDetector
import screen_brightness_control as sbc
from math import hypot
  
# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.29.8:8080/shot.jpg"

#create object detector
detector= HandDetector(detectionCon=0.8)

# While loop to continuously fetching data from the Url
while True:
	img_resp = requests.get(url)#we use request module to get live video feed
	img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)#converting it to np array for easier mathematical computation
	img = cv2.imdecode(img_arr, -1)
	img = imutils.resize(img, width=1000, height=1800)#resizing images
	
	hands,img= detector.findHands(img)#going to return img with drawing
	
	#for each hand we'll have info like Hand-->dict{lmList,boundingbox,center,type}
	if hands: 
		hand1=hands[0]#gives us first hand
		lmList1=hand1["lmList"]# List of 21 landmarks
		bbox1=hand1["bbox"]#x,y,w,h of bounding box
		centerPoint1=hand1["center"]#center of the hand cx,cy
		handType1=hand1["type"]#left or right

		finger1=detector.fingersUp(hand1)

		length,info,img=detector.findDistance(lmList1[4],lmList1[8],img)
		
		bright = np.interp(length,[15,220],[0,100])
		# Hand range 15 - 220
		# Brightness range 0 - 100
		print(bright,length)
		sbc.set_brightness(int(bright))
		 
	if len(hands)==2:
		hand2=hands[1]#gives us second hand
		lmList2=hand2["lmList"]# List of  21 landmarks
		bbox2=hand2["bbox"]#x,y,w,h of bounding box
		centerPoint2=hand2["center"]#center of the hand cx,cy
		handType2=hand2["type"]#left or right
		finger2=detector.fingersUp(hand2)
		length,info,img=detector.findDistance(lmList2[4],lmList2[8],img)
		bright = np.interp(length,[15,220],[0,100])
		print(bright,length)
		sbc.set_brightness(int(bright))
	    # Hand range 15 - 220
		# Brightness range 0 - 100

	cv2.imshow("Android_cam", img)
  
	#Wait for user input - q, then you will stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF #it will wait for 1 mili second bitwise and 
	if key_pressed == ord('q'): #ord tells you ascii value of that character
		break
  
cv2.destroyAllWindows()