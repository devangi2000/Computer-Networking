import socket
s = socket.socket(type=socket.SOCK_DGRAM)
host= '127.0.0.1'
port= 5002
s.bind((host,port))
print('Client waiting for a message...')
while True:
    data, addr = s.recvfrom(1024)
    if data.decode()=="bye":
        print('Stopped')
        break
    s.sendto(data, addr)
s.close()

