import cv2
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)
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
		length,info,img=detector.findDistance(lmList1[8],lmList1[12],img)
		 
	if len(hands)==2:
		hand2=hands[1]#gives us second hand
		lmList2=hand2["lmList"]# List of  21 landmarks
		bbox2=hand2["bbox"]#x,y,w,h of bounding box
		centerPoint2=hand2["center"]#center of the hand cx,cy
		handType2=hand2["type"]#left or right
		finger2=detector.fingersUp(hand2)
		length,info,img=detector.findDistance(lmList1[8],lmList2[8],img)
		length,info,img=detector.findDistance(centerPoint1,centerPoint2,img)



	cv2.imshow("Image",img)


	#Wait for user input - q, then you will stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF #it will wait for 1 mili second bitwise and 
	if key_pressed == ord('q'): #ord tells you ascii value of that character
		break

cap.release()
cv2.destroyALlWindows()