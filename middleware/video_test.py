import argparse
import os
import sys
import time

import numpy as np

import cv2
from thre import WebcamStream


def video_face():
    face = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
    eye = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')
   # body = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_upperbody.xml')
    # vid = cv2.VideoCapture(0)
    vid = WebcamStream(src=0)
    vid.start()
    while(1):
        frame = vid.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face1 = face.detectMultiScale(gray, 1.3, 5)
      #  body1 = body.detectMultiScale(gray,1.3,5)

        for(x, y, w, h) in face1:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + h]
            roi_color = frame[y:y + h, x:x + w]
           # face1 = face.detectMultiScale(gray,1.3,5)
            eyes = eye.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        resz = cv2.resize(frame, (640, 480))
        vid.rea().write(frame)
        cv2.imshow('img', resz)

        for i in frame:
            m = i.tostring()
            # print(m)
            sys.stdout.write(m)
            #os.write(1, m)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cv2.destroyAllWindows()
    vid.stop()

if __name__ == "__main__":
    video_face()
