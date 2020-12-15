import socket
import os
import re
s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(('localhost', 9999))
arp_table={}

data = s.recvfrom(1024)
ip_address=data[0].decode()
destination=data[1]
with os.popen('arp -a') as f:
    data=f.read()
    #print(data)

for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',data):
    arp_table[line[0]]=line[1]

if(ip_address in arp_table):
    s.sendto(arp_table[ip_address].encode(), destination)
else:
    print(ip_address," is not present in the ARP Table")

s.close()