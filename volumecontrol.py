import cv2
from cvzone.HandTrackingModule import HandDetector
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
	IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volRange= volume.GetVolumeRange()
minvol=volRange[0]
maxvol=volRange[1]
vol=0
volBar=0

cap=cv2.VideoCapture(0)#getting our web camera

#create object detector
detector= HandDetector(detectionCon=0.8)


while True:
	success,img=cap.read()
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
		vol = np.interp(length,[15,220],[minvol,maxvol])
		volBar = np.interp(length,[50,300],[400,150])
		# Hand range 15 - 220
		# Volume range 0 - 100
		print(vol,length)
		volume.SetMasterVolumeLevel(vol, None)
	if len(hands)==2:
		hand2=hands[1]#gives us second hand
		lmList2=hand2["lmList"]# List of  21 landmarks
		bbox2=hand2["bbox"]#x,y,w,h of bounding box
		centerPoint2=hand2["center"]#center of the hand cx,cy
		handType2=hand2["type"]#left or right
		finger2=detector.fingersUp(hand2)
		length,info,img=detector.findDistance(lmList2[4],lmList2[8],img)
		vol = np.interp(length,[15,220],[minvol,maxvol])
		volBar = np.interp(length,[50,300],[400,150])
		# Hand range 15 - 220
		# Volume range 0 - 100
		print(vol,length)
		volume.SetMasterVolumeLevel(vol, None)


	cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
	cv2.rectangle(img,(50,int(volBar)),(85,400),(255,0,0),cv2.FILLED)
	cv2.imshow("Image",img)


	#Wait for user input - q, then you will stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF #it will wait for 1 mili second bitwise and 
	if key_pressed == ord('q'): #ord tells you ascii value of that character
		break

cap.release()
cv2.destroyALlWindows()