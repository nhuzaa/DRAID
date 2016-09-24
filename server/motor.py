import RPi.GPIO as GPIO

IN1 = 19
IN2 = 20
IN3 = 21
IN4 = 22

ENA = 23
ENB = 24

GPIO.setmode(GPIO.BCM)


class motorDriver:
    GPIO.setup(IN1, GPIO.OUT)  # OUT1 LEFT RED
    GPIO.setup(IN2, GPIO.OUT)  # OUT2 LEFT BLACK
    GPIO.setup(IN3, GPIO.OUT)  # OUT3 RIGHT RED
    GPIO.setup(IN4, GPIO.OUT)  # OUT4 RIGHT BLACK

    GPIO.setup(ENA, GPIO.OUT)  # Enable PIN LEFT
    GPIO.setup(ENB, GPIO.OUT)  # Enable PIN RIGHT

    pwma = GPIO.PWM(ENA, 100)
    pwmb = GPIO.PWM(ENB, 100)

    def __init__(self):

        self.pluseEnable()
        self.enableHigh()

    def pluseEnable(self):

        self.pwma.start(75)
        self.pwmb.start(75)

        # PWMA.ChangeDutyCycle(12.5)
        # PWMB.ChangeDutyCycle(12.5)

    def pluseDisable(self):
        self.pwma.stop()
        self.pwmb.stop()

    def enableHigh(self):
        GPIO.output(ENA, GPIO.HIGH)
        GPIO.output(ENB, GPIO.HIGH)

    def enableLow(self):
        GPIO.output(ENA, GPIO.LOW)
        GPIO.output(ENB, GPIO.LOw)

    def forward(self):
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)

    def backward(self):
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)

    def left(self):
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)

    def right(self):
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)

    def stop(self):
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)

    def brake(self):
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.HIGH)
