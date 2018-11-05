from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.bind(('',5678))
s.connect(('10.114.30.212',8080))
while True:
    msg=input('内容：')
    s.send(msg.encode('utf8'))
    data=s.recv(1024)
    print(data.decode('utf8'))