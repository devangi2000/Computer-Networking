import socket
import getmac

s= socket.socket(type=socket.SOCK_DGRAM)
s.bind(('localhost',9999))

data = s.recvfrom(1024)
ip_address=data[0].decode()
destination=data[1]

mac = getmac.get_mac_address(ip=ip_address)

if mac is not None:
    s.sendto(mac.encode(),destination)
else:
    s.sendto("Not found".encode(),destination)
s.close()