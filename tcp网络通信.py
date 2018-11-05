#tcp套接字
from socket import *
s=socket(AF_INET,SOCK_STREAM)
#绑定端口
s.bind(('',4568))
#监听
s.listen(5)
#等待连接
s1,address=s.accept()

#接收消息
while True:
    data=s1.recv(1024)
    s1.send('你好'.encode('utf8'))
    print(address)
    print(data.decode('utf8'))
#发送消息

s1.close()
s.close()
