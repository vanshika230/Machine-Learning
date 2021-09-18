# Read a Video Stream from Camera(Frame by Frame)
import cv2

cap = cv2.VideoCapture(0) #0 means default web cam
# Face Detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
	ret,frame = cap.read() #cap.read reads frame and returns a boolean value and the frame

	if ret == False:                                         
		continue #can be due to unavailability of webcam etc

	faces = face_cascade.detectMultiScale(frame,1.3,5) #scalingfactor-resizes img to the size of img which was used to train the data ,no.ofneighbours
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		
	cv2.imshow("Video Frame",frame)

	#Wait for user input - q, then you will stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF #it will wait for 1 mili second bitwise and 
	if key_pressed == ord('q'): #ord tells you ascii value of that character
		break

cap.release()
cv2.destroyALlWindows()


