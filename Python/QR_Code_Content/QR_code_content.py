#! /usr/bin/python3
import numpy as np
from numpy.core.fromnumeric import size
import pyperclip
import cv2
import sys
from pyzbar.pyzbar import decode


def webcamCap(inputD):

    # Webcam Capture
    capture_stream = cv2.VideoCapture(inputD)
    capture_stream.set(3, 640)
    capture_stream.set(3, 480)
    ans = ""
    while True:

        success, img = capture_stream.read()

        for code in decode(img):
            # Data in  code
            ans = code.data.decode('utf-8')
            # Coordinates of polygon over the QR code
            points = np.array([code.polygon], np.int32)
            points = points.reshape((-1, 1, 2))
            cv2.polylines(img, [points], True, (255, 0, 255), 5)

            # points for rectangle
            pts2 = code.rect
            cv2.putText(img, ans, (pts2[0], pts2[1]),
                        cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 255), thickness=2)

        cv2.imshow("Result ", img)
        if cv2.waitKey(20) & 0xFF == ord("c"):
            print(ans)
            pyperclip.copy(ans)
            break


def imgCap(img):
    ans = ""

    img = (cv2.imread(img))

    ans = decode(img)[0].data.decode("utf-8")
    stats = decode(img)[0]
    # Coordinates of polygon over the QR code
    points = np.array([stats.polygon], np.int32)
    points = points.reshape((-1, 1, 2))
    cv2.polylines(img, [points], True, (255, 0, 255), 5)

    # points for rectangle
    pts2 = stats.rect
    cv2.putText(img, ans, (pts2[0], pts2[1]),
                cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 255), thickness=2)
    while True:
        cv2.imshow("Result ", img)
        if cv2.waitKey(20) & 0xFF == ord("c"):
            print(ans)
            pyperclip.copy(ans)
            break


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Get subject from command line.
        img = sys.argv[1]
        imgCap(img)
    else:
        webcamCap(0)
