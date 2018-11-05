from threading import Thread
# import  time
# 函数
# def say():
#     time.sleep(1)
#     print('我错了')
# for i in range(5):
#     t = Thread(target=say)
#     t.start()
# print('11')


# 类的线程
# class My_zxx(Thread):
#     def run(self):
#         for i in range(3):
#             time.sleep(1)
#             print('哈哈')
# t=My_zxx()
# t.start()


#线程共享全局变量
# num = 0
# def text1():
#     global num
#     num += 1
#     time.sleep(1)
#     print('text1',num)
# def text2():
#     time.sleep(3)
#     print('text2',num)
# t1=Thread(target=text1)
# t1.start()
# t2=Thread(target=text2)
# t2.start()

#局部变量不共享
# import threading
# def text1():
#     num = 0
#     if threading.currentThread().name=='Thread-1':
#         num+=1
#         time.sleep(1)
#         print('threading-1',num)
#     else:
#         time.sleep(3)
#         print(num)
#
# t1=Thread(target=text1)
# t1.start()
# t2=Thread(target=text2)
# t2.start()


#线程修改全局变量(非安全的),然后加锁
# num=0
# flag=True
# def text1():
#
#     global num
#     global flag
#     if flag:
#         for i in range (1000000):
#             num+=1
#         flag=False
#     print(num)
# def text2():
#     global num
#     global flag
#     while True:
#         if not flag:
#             for i in range(1000000):
#                 num += 1
#             flag=True
#             break
#     print(num)
# t1=Thread(target=text1)
# t1.start()
# # time.sleep(1)
# t2=Thread(target=text2)
# t2.start()


#互斥锁
from threading import Lock
num=0
m=Lock()
def text1():
    global num
    for i in range (1000000):
        m.acquire()
        num+=1
        m.release()
    print(num)
def text2():
    global num
    for i in range(1000000):
        m.acquire()
        num += 1
        m.release()
    print(num)
t1=Thread(target=text1)
t1.start()
t2=Thread(target=text2)
t2.start()
