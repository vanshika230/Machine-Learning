import cv2 as cv

img = cv.imread('me.jpg')


def rescaleFrame(frame, scale=0.2):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)

	dimensions = (width,height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_img=rescaleFrame(img)
cv.imshow('Mebig', img)
cv.imshow('Me', resized_img)

cv.waitKey(0)
cv.destroyAllWindows()