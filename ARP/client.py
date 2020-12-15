import socket

c = socket.socket(type=socket.SOCK_DGRAM)

c.connect(('localhost',9999))

ip_address = socket.gethostbyname(socket.gethostname())
c.sendto(ip_address.encode(),('localhost',9999))
mac_address=c.recvfrom(1024)
print(mac_address[0].decode())
c.close()