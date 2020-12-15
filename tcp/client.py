import socket
s = socket.socket()
port = 8990

s.connect(('127.0.0.1', port))

print("Client Waiting....")
while True:
    msg = s.recv(1024)
    if len(msg)>0:
        print("Server: " + msg.decode())
        l=input("Feedback: ")
        s.send(str.encode(l))
    else:
        s.close()
        break
