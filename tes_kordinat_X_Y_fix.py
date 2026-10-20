import cv2 
import numpy as np

def nothing(x):
    pass

video = cv2.VideoCapture(0)

# 1. BUAT JENDELA DAN TRACKBAR DI LUAR LOOP (Hanya dibuat sekali saja)
cv2.namedWindow("Tracking")

cv2.createTrackbar("LH", "Tracking", 30, 179, nothing)
cv2.createTrackbar("LS", "Tracking", 40, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 100, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 85, 179, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    success, img = video.read()
    if not success:
        break

    # 2. AMBIL NILAI TRACKBAR DI DALAM LOOP
    lh = cv2.getTrackbarPos("LH", "Tracking")
    ls = cv2.getTrackbarPos("LS", "Tracking")
    lv = cv2.getTrackbarPos("LV", "Tracking")
    uh = cv2.getTrackbarPos("UH", "Tracking")
    us = cv2.getTrackbarPos("US", "Tracking")
    uv = cv2.getTrackbarPos("UV", "Tracking")

    lower = np.array([lh, ls, lv])
    upper = np.array([uh, us, uv])
        
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lower, upper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 100:
                # 1. Bikin Kotak
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

                # 2. Hitung Titik Tengah
                cx = x + w // 2
                cy = y + h // 2

                # 3. Garis Silang Sumbu X & Y
                cv2.line(img, (cx, 0), (cx, img.shape[0]), (0, 0, 255), 2)
                cv2.line(img, (0, cy), (img.shape[1], cy), (0, 0, 255), 2)

                # 4. Munculkan Teks Koordinat (SUDAH DIPERBAIKI)
                text_tampil = f"X : {cx}, Y : {cy}"
                cv2.putText(img, text_tampil, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                print(f"kordinat objek -> X : {cx}, Y : {cy}")

    cv2.imshow("mask", mask)
    cv2.imshow("img", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()