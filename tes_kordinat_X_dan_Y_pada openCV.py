import cv2 
import numpy as np

lower = np.array ([0,100,10])
upper = np.array ([35,255,255])

video = cv2.videoCapture(0)

while True :
success, img = video.read()
image = cv2.cvtColor (img, cv2.COLOR_BGR2HSV)
mask = CV2.inRange (image, lower, upper)

countours, hierarcy = cv2.findCountours (mask, cv2.RETR_EXTERNAL, CV2.CHAIN_APPROX_SIMPLE)

if len (contours) != 0:
    for countours:
    if cv2.countourArea(countour)>500:
        x,y,w,h = cv2.boundingrect (contour)
        cv2.rectangle (img, (x,y), (x + w, y + h) 3, (0,255,0),3)

        cv2.imshow("mask", mask)
        cv2.imshow("img, "img)

cv2.waitkey(1)