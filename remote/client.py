import socket

s = socket.socket(type=socket.SOCK_DGRAM)

s.connect(('127.0.0.1', 4545))

command = input('Enter a system command: ')
s.sendto(command.encode(), ('localhost', 4545))

s.close()

#some useful commands to know: ipconfig, netstat, ping google.com, tracert,
# powercfg, shutdown, systeminfo, sfc, schtasks,