import socket
from time import ctime
import threading

sADDR = ("127.0.0.1", 45002)
buff = 1024

servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servSock.bind(sADDR)
servSock.listen(5)

print("Waiting for a connection...")
cliSock, cADDR = servSock.accept()
print("...Connection made with {0}".format(cADDR))

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
        if not sMessage:
            break
        cliSock.send(sMessage.encode())

t1 = threading.Thread(target=send, name=3)
t2 = threading.Thread(target=receive, name=4)

t1.start()
t2.start()