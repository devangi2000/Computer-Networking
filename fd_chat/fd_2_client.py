import socket
from time import ctime
import threading

sADDR = ('127.0.0.1', 45002)
buff = 1024

cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliSock.connect(sADDR)

def receive():
    while True:
        rMessage = cliSock.recv(buff)
        if not rMessage:
            print("Ending connection")
            break
        print("[{0}]: {1}".format(ctime(), rMessage.decode()))

def send():
    while True:
        sMessage = input(">>")
        cliSock.send(sMessage.encode())

t1 = threading.Thread(target=send, name=1)
t2 = threading.Thread(target=receive, name=2)

t1.start()
t2.start()