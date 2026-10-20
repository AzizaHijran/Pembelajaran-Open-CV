import cv2
import numpy as np

lower = np.array ([30, 10, 5])
upper = np.array ([85, 255, 255])

video = cv2.VideoCapture(0)

while True : 
    success, img = video.read()   
    image = cv2.cvtColor (img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange (image, lower, upper)
    
    contours, hierarcy = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # CHAIN_APPROX_SIMPLE hanya menyimpan semua kordinat kontur yang diperlukan
    #  CHAIN_APPROX_NONE hanya menyimpansetiapkordinat tepi luar kontur

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect (contour)
                cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 3)
    

    cv2.imshow ("mask", mask)
    cv2.imshow ("capture", img)

    cv2.waitKey(1)
        