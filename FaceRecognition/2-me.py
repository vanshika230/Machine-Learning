import cv2 #importing open cv

img = cv2.imread("me.jpg") #reading image
gray = cv2.imread('me.jpg',cv2.IMREAD_GRAYSCALE)# reading image as gray scale

cv2.imshow('image',img) #title to be given, image 
cv2.imshow('gray',gray)
#Wait for any key before image disappears

cv2.waitKey(0)#weight for infinite time(until a key is pressed)
cv2.destroyAllWindows()