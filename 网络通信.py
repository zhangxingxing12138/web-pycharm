#创建Udp的套接字
from threading import Thread
import time
from socket import *
s=None
# ip=''
# port=''
def main():
    global s,id,port
    # ip=input('ip:')
    # port=int(input('port:'))
    s = socket(AF_INET, SOCK_DGRAM)
    # s.bind(('',4592))
def send():
    while True:
        msg=input('输入内容\n')
        s.sendto(msg.encode('gb2312'),('10.114.30.195',8080))
def receive():
    while True:
        data=s.recvfrom(1024)
        print('%s         \n%s'%(data[0].decode('gb2312'),'请输入发送内容'),end='')
        # , data[1][0], data[1][1]
    # s.close()
if __name__=='__main__':
    main()
    s1=Thread(target=send)
    s1.start()

    s2=Thread(target=receive)
    s2.start()

