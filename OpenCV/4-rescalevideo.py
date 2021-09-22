import cv2 as cv

def rescaleFrame(frame, scale=0.75):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)

	dimensions = (width,height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading Videos
capture = cv.VideoCapture('detector.mp4')

while True:
	isTrue, frame = capture.read()

	frame_resized = rescaleFrame(frame, scale=.2)
	
	cv.imshow('Video', frame)#show original video
	cv.imshow('Video Resized', frame_resized)#show resized video

	if cv.waitKey(20) & 0xFF==ord('d'):
		break

capture.release()
cv.destroyAllWindows()