import cv2 as cv

capture = cv.VideoCapture('detector.mp4')
#THIS IS USED TO READ A VIDEO THAT YOU ALREADY HAVE
#capture = cv.VideoCapture(0)is used to capture webcamera video

while True:
	isTrue, frame = capture.read()
	#it returns a boolean which tells if reading the fram was successful or not, frame
	cv.imshow('video',frame)

	#Wait for user input - q, then you will stop the loop
	key_pressed = cv.waitKey(20) & 0xFF #it will wait for 1 mili second bitwise and 
	if key_pressed == ord('q'): #ord tells you ascii value of that character
		break

capture.release()
cv2.destroyALlWindows()