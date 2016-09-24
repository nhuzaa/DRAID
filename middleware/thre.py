from threading import Thread

import cv2


class WebcamStream:

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(0)
        #self.stream = cv2.VideoCapture(src)
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        self.video = cv2.VideoWriter('video.avi', fourcc, 30, (640, 480))
        (self.ret, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            (self.ret, self.frame) = self.stream.read()

    def read(self):
        return self.frame

    def rea(self):
        return self.video

    def stop(self):
        self.stopped = True
