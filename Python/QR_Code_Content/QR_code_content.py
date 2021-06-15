import numpy as np
import cv2
from pyzbar.pyzbar import decode


# Webcam Capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(3, 480)

while True:

    success, img = cap.read()

    for barcode in decode(img):
        # Data in Bar code
        myData = barcode.data.decode('utf-8')
        print(myData)

        # Coordinates of polygon over the QR code
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)

        # points for rectangle
        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1]),
                    cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 0, 255))

    cv2.imshow("Result ", img)
    cv2.waitKey(1)
