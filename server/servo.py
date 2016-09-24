import time

import RPi.GPIO as GPIO

pinout1 = 16
pinout2 = 4
# pinout3 = 22
# pinout4 = 24

GPIO.setmode(GPIO.BCM)


GPIO.setup(pinout1, GPIO.OUT)
GPIO.setup(pinout2, GPIO.OUT)
# GPIO.setup(pinout3, GPIO.OUT)
# GPIO.setup(pinout4, GPIO.OUT)


p1 = GPIO.PWM(pinout1, 50)
p2 = GPIO.PWM(pinout2, 50)
# p3 = GPIO.PWM(pinout3, 50)
# p4 = GPIO.PWM(pinout4, 50)

p1.start(7.5)
p2.start(7.5)
# p3.start(7.5)
# p4.start(7.5)


try:
    # while 1:
    # 	time.sleep(2)
    # 	p1.ChangeDutyCycle(10.5)
    # 	p2.ChangeDutyCycle(10.5)
    # 	time.sleep(2)
    # 	p1.ChangeDutyCycle(4.5)
    # 	p2.ChangeDutyCycle(4.5)
    # 	time.sleep(2)
    # 	p1.ChangeDutyCycle(7.5)
    # 	p2.ChangeDutyCycle(7.5)

    x = 7.5
    while 1:
        print("forward")
        while(x <= 10.5):
            x = x + 0.25
            print(x)
            p2.ChangeDutyCycle(x)
            p1.ChangeDutyCycle(x)
            time.sleep(0.05)
        time.sleep(1)
        print("reverse")
        while(x >= 4.5):
            x = x - 0.25
            print(x)
            p2.ChangeDutyCycle(x)
            p1.ChangeDutyCycle(x)
            time.sleep(0.05)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
