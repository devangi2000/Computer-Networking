import socket
import os

s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 4545))

data = s.recvfrom(1024)
os.system('cmd/c "{}"'.format(data[0].decode()))

s.close()