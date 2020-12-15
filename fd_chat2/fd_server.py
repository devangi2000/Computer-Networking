import socket
import threading
sADDR = ("127.0.0.1", 9999)
buff = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(sADDR)
s.listen(5)

print ("Waiting for a connection...")
c, cADDR = s.accept()
print ("...Connection made with {0}".format(cADDR))

def receive():
    while True:
        rMessage = c.recv(buff)
        if (rMessage.decode() == 'stop'):
            print ("Ending connection")
            return 0
        print ('client:',rMessage.decode())

def send():
    while True:
        sMessage = input("message: ")
        if sMessage == 'stop':
            c.sendall(sMessage.encode())
            print("Ending the connection")
            return 0
        c.sendall(sMessage.encode())

t1 = threading.Thread(target=send, name=3)
t2 = threading.Thread(target=receive, name=4)

t1.start()
t2.start()