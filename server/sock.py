import socket
import sys

from _thread import *
from motor import motorDriver
from servoctrl import servo

m = motorDriver()
servo = servo()

host = ''
port = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
print("Waiting for the connection")


def threaded_client(conn, addr):
    conn.send(str.encode("welcome, type your info\n"))

    while True:
        data = conn.recv(4096)
        c = data.decode('utf-8')
        print(c)
        if(c[0] != 'x'):
            if c == "w":
                print("forward")
                m.forward()
            elif c == "a":
                print("left")
                m.left()
            elif c == 'd':
                print("right")
                m.right()
            elif c == 's':
                print("backward")
                m.backward()
            elif c == 'b':
                print("brake")
                m.brake()
            elif c == 'i':
                servo.yServoUp()
            elif c == 'k':
                servo.yServoDown()
            elif c == 'j':
                servo.xServoUp()
            elif c == 'l':
                servo.xServoDown()
            elif c == 'r':
                servo.reset()
            elif not data:
                m.stop()
            else:
                print("not valid")
                m.stop()
        else:
            xval = int(c[1])
            yval = int(c[2])

            if(0 <= xval <= 9 and 0 <= yval <= 9):
                if yval > 5:
                    servo.yServoDown()
                elif yval < 5:
                    servo.yServoUp()

                if xval > 5:
                    servo.xServoDown()
                elif xval < 5:
                    servo.xServoUp()
            else:
                print("not valid servo cordinates")
        conn.sendall(str.encode(c))

    conn.close()
while True:

    conn, addr = s.accept()
    print('connected to :' + addr[0] + ':' + str(addr[1]))

    start_new_thread(threaded_client, (conn, addr))
