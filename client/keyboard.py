import socket

import numpy as np
import pygame

pygame.init()
pygame.display.init()
pygame.display.set_mode((640, 480))
pygame.key.set_repeat(1, 50)


HOST = '192.168.1.101'
PORT = 6666


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))
print("connection done")
while 1:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("brake")
                conn.send(str.encode("b"))

            if event.key == pygame.K_a:
                print("left")
                conn.send(str.encode("a"))

            if event.key == pygame.K_w:
                print("forward")
                conn.send(str.encode("w"))

            if event.key == pygame.K_s:
                print("reverse")
                conn.send(str.encode("s"))

            if event.key == pygame.K_d:
                print("right")
                conn.send(str.encode("d"))
# Servo
            if event.key == pygame.K_i:
                print("Skervo Y up - u")
                while(event.type != pygame.KEYUP):
                    conn.send(str.encode("u"))
                    event = pygame.event.get()

            if event.key == pygame.K_k:
                print("Servo Y down - j")
                while(event.type != pygame.KEYUP):
                    conn.send(str.encode("j"))
                    event = pygame.event.get()

            if event.key == pygame.K_j:
                print("Servo X up - i ")
                while(event.type != pygame.KEYUP):
                    conn.send(str.encode("i"))
                    event = pygame.event.get()

            if event.key == pygame.K_l:
                print("Servo X down -  k")
                while(event.type != pygame.KEYUP):
                    conn.send(str.encode("k"))
                    event = pygame.event.get()
        if event.type == pygame.KEYUP:
            conn.send(str.encode("b"))
            print("stop")
