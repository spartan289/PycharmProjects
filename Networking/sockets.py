import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('localhost', 9000))
cmd = 'GET / HTTP/1.1\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode(),end='')
mysock.close()
