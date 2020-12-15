import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host= '127.0.0.1'
port= 5002
s.connect((host,port))
while True:
    d= input("Enter text: ")
    s.sendto(d.encode(), (host, port))
    d = s.recvfrom(1024)
    if d[0].decode()!="bye":
        print('Server echoed ' + d[0].decode())
    else:
        print('Stopping...')
        break
s.close()
