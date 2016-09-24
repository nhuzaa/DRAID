import socket

import pygame

HOST = '192.168.12.1'
PORT = 6666

pygame.joystick.init()
pygame.display.init()
if not pygame.joystick.get_count():
    print("\nPlease connect a joystick and run again.\n")
    quit()
print("\n%d joystick(s) detected." % pygame.joystick.get_count())
joy = pygame.joystick.Joystick(0)
joy.init()
print("Ready for Action\n")

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))
print("connection done")


while True:
    event = pygame.event.wait()
    if event.type == pygame.JOYBUTTONDOWN:
        if joy.get_button(0) == 1:
            print("forward")
            conn.send(str.encode("w"))
        if joy.get_button(2) == 1:
            print("reverse")
            conn.send(str.encode("s"))
        if joy.get_button(3) == 1:
            print("left")
            conn.send(str.encode("a"))
        if joy.get_button(1) == 1:
            print("right")
            conn.send(str.encode("d"))

        # servoBase
        if joy.get_button(6) == 1:
            print("Skervo Y up - i")
            conn.send(str.encode("i"))
        if joy.get_button(7) == 1:
            print("Servo Y down - j")
            conn.send(str.encode("k"))
         # servoA and servo B
        if joy.get_button(10) == 1:
            print("Servo X up - j ")
            conn.send(str.encode("j"))

        if joy.get_button(11) == 1:
            print("Servo X up - l ")
            conn.send(str.encode("l"))
        if joy.get_button(5) == 1:
            print("Servo Reset - r")
            conn.send(str.encode("r"))
        # # tuin
        # if self.joy.get_button(10) == 1 or self.joy.get_button(11) == 1:
        #     print("automatic")
        #     return 1

    if event.type == pygame.JOYBUTTONUP:
        conn.send(str.encode("b"))
        print("stop")
