# from greenlet import greenlet
# import time
# #coding=utf-8
# def test1():
#     while True:
#         print('----A----')
#         gr2.switch()
#         time.sleep(0.5)
#
# def test2():
#     while True:
#         print('----B----')
#         gr1.switch()
#         time.sleep(0.5)
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
#
# #切换到gr1中运行
# gr1.switch()

import time
import gevent
from gevent import monkey
monkey.patch_all()#补丁
def f1(n):
    for i in range(n):
        print(i)
        time.sleep(1)
        # gevent.sleep(0.5)
def f2(n):
    for i in range(n):
        print(i)
        time.sleep(1)
        # gevent.sleep(0.5)#阻塞操作

# g1 = gevent.spawn(f1, 5)
# g2 = gevent.spawn(f1, 5)

# g1.join()
# g2.join()
gevent.joinall([
        gevent.spawn(f1, 5),
        gevent.spawn(f2, 5),
])
