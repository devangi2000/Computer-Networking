import socket

c = socket.socket(type=socket.SOCK_DGRAM)

c.connect(('localhost',9999))

ip_address = input("Enter system ip address: ")
#ip_address = socket.gethostbyname(socket.gethostname())
c.sendto(ip_address.encode(),('localhost',9999))
mac_address = c.recvfrom(1024)
print("mac address: ",mac_address[0].decode())
c.close()