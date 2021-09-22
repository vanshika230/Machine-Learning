#reading images using OpenCV
import cv2 as cv
img=cv.imread('me.jpg')#reading
cv.imshow('Me',img)#displaying
cv.waitKey(0)#waits for infinity time for the user to press a key and exit the window
