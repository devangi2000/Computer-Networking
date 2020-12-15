import socket

s = socket.socket()
host = socket.gethostname()
port = 8066
s.bind((host,port))
print(host)
s.listen(1)

print('Awaiting connection...')
conn, addr = s.accept()
print('Connected to the server ', addr)

filename = input(str('Please enter the name of the file: '))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print('Data transmission successful!')