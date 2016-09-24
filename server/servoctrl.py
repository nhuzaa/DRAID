import time

import RPi.GPIO as GPIO

pinoutX = 16
pinoutY = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(pinoutX, GPIO.OUT)
GPIO.setup(pinoutY, GPIO.OUT)

pX = GPIO.PWM(pinoutX, 50)
pY = GPIO.PWM(pinoutY, 50)


class servo:

    xPos = 7.5
    yPos = 7.5

    def __init__(self):
        pX.start(self.xPos)
        pY.start(self.yPos)

    def yServoUp(self):
        if(self.yPos <= 10.5 and self.yPos >= 4.5):
            self.yPos = self.yPos + 0.25
            print("Yservo " + str(self.yPos))
            pY.ChangeDutyCycle(self.yPos)
            time.sleep(0.02)
        else:
            self.limit()

    def xServoUp(self):
        if(self.xPos <= 10.5 and self.xPos >= 4.5):
            self.xPos = self.xPos + 0.25
            print("xservo " + str(self.xPos))
            pX.ChangeDutyCycle(self.xPos)
            time.sleep(0.02)
        else:
            self.limit()

    def yServoDown(self):
        if(self.yPos <= 10.5 and self.yPos >= 4.5):
            self.yPos = self.yPos - 0.25
            print("Yservo " + str(self.yPos))
            pY.ChangeDutyCycle(self.yPos)
            time.sleep(0.02)
        else:
            self.limit()

    def xServoDown(self):
        if(self.xPos <= 10.5 and self.xPos >= 4.5):
            self.xPos = self.xPos - 0.25
            print("xservo " + str(self.xPos))
            pX.ChangeDutyCycle(self.xPos)
            time.sleep(0.02)
        else:
            self.limit()

    def setxServo(self, angle):
        self.xPos = map(angle)
        pX.ChangeDutyCycle(self.xPos)
        print("xservo " + str(self.xPos))

    def setyServo(self, angle):
        self.yPos = map(angle)
        pY.ChangeDutyCycle(self.yPos)
        print("Yservo " + str(self.yPos))

    def reset(self):
        self.xPos = 7.0
        self.yPos = 7.5
        pX.ChangeDutyCycle(self.xPos)
        pY.ChangeDutyCycle(self.yPos)
        print("Servo RESET Bro xpos:" + str(self.xPos) + " ypos :" + str(self.yPos))

    def map(self, angle):

        percent = angle / 180

        pluse = percent * (10.5 - 4.5)
        pluse = pluse + 4.5

        return pluse

    def limit(self):
        if(self.yPos > 10.5):
            self.yPos = 10.5
        elif(self.yPos < 4.5):
            self.yPos = 4.5

        if(self.xPos > 10.5):
            self.xPos = 10.5
        elif(self.xPos < 4.5):
            self.xPos = 4.5
