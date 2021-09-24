# Control Laptop Brightness with fingers via Phone camera

## 1. Installation
Open command line and enter the following command :
```
pip install media pipe
pip install screen_brightness_control
pip install imutils
```
works well if you already have anaconda packages installed, otherwise look at the code and google search on how to import the required stuff😅 don't be dissapointed in this guide- that's mostly how coding works😃🤷‍♀️
```
# Import essential libraries
import requests
import cv2
import numpy as np
import imutils
from cvzone.HandTrackingModule import HandDetector
import screen_brightness_control as sbc
from math import hypot
```
## 2. Getting our Android phone camera live feed on our computer
 a. Download IP Webcam app from playstore. 
 
 b. Click on Start Server (usually at the end)
 
 c. Look at the screen it will display links like this :- http://192.168.29.8:8080
 
 d. carefully note your link and paste it on your browser search 
 
 e. It will open a new window
 
 f. In video rendering click on javascript
 
 g. Voila! you'll now be able to see you phone camera feed on your laptop
 
 ```
 # Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.29.8:8080/shot.jpg" #paste your link here, add shot.jpg just like this
 ```
That's it for the pre code stuff, now head on over to the code and decipher everything from the comments and google. All the best!


