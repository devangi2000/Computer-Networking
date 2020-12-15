import socket
from time import ctime
import threading

sADDR = ('127.0.0.1', 9999)
buff = 1024

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(sADDR)

def receive():
    while True:
        rmes = c.recv(buff)
        if rmes.decode() == 'stop':
            print("Ending the connection")
            return 0
        print('server: ',rmes.decode())

def send():
    while True:
        mes = input("message: ")
        if mes == 'stop':
            c.sendall(mes.encode())
            print("Ending the connection")
            return 0
        c.sendall(mes.encode())

t1 = threading.Thread(target = send, name = 1)
t2 = threading.Thread(target = receive, name = 2)

t1.start()
t2.start()