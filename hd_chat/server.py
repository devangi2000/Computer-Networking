import socket
s = socket.socket()
port = 8991
s.bind(('127.0.0.1',port))
print('Waiting for request...')
s.listen(10)
conn, addr = s.accept()
while True:
    data = input('Enter request:')
    if data == "bye":
        conn.close()
        s.close()
        break
    print('Request received from ', addr)
    if len(str.encode(data))>0:
        conn.send(str.encode(data))
        d = str(conn.recv(1024), "utf-8")
        print("Client: "+d+"\n",end="")
conn.close()