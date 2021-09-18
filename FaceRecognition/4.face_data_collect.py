# Write a Python Script that captures images from your webcam video stream
# Extracts all Faces from the image frame (using haarcascades)
# Stores the Face information into numpy arrays

# 1. Read and show video stream, capture images
# 2. Detect Faces and show bounding box (haarcascade)
# 3. Flatten the largest face image(gray scale) and save in a numpy array
# 4. Repeat the above for multiple people to generate training data


# Read a Video Stream from Camera(Frame by Frame)
import cv2
import numpy as np

cap = cv2.VideoCapture(0) #0 means default web cam
# Face Detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
skip = 0
face_data = []
dataset_path = './data/'
file_name = input("Enter the name of the person : ")

while True:
	ret,frame = cap.read() #cap.read reads frame and returns a boolean value and the frame

	if ret == False:                                         
		continue #can be due to unavailability of webcam etc

	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	
	faces = face_cascade.detectMultiScale(frame,1.3,5)#each face is a tuple, tuples are saved in list
	faces = sorted(faces,key=lambda f:f[2]*f[3])

    # Pick the last face (because it is the largest face acc to area(f[2]*f[3]))
	for face in faces[-1:]:
		x,y,w,h = face
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

		#Extract (Crop out the required face) : Region of Interest
		offset = 10
		face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
		face_section = cv2.resize(face_section,(100,100))

		skip += 1
		if skip%10==0:
			face_data.append(face_section)
			print(len(face_data))



	cv2.imshow("Frame",frame) 
	#cv2.imshow("Face Section",face_section)

	#Wait for user input - q, then you will stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF #it will wait for 1 mili second bitwise and 
	if key_pressed == ord('q'): #ord tells you ascii value of that character
		break


# Convert our face list array into a numpy array
face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)

# Save this data into file system
np.save(dataset_path+file_name+'.npy',face_data)
print("Data Successfully save at "+dataset_path+file_name+'.npy')

cap.release()
cv2.destroyALlWindows()








