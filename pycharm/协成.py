import time
#协成是通过生成器的方式实现的
def work1():
    while True:
        print("----work1---")
        yield
        time.sleep(0.5)

def work2():
    while True:
        print("----work2---")
        yield
        time.sleep(1)
w1 = work1()
w2 = work2()
while True:
    next(w1)
    next(w2)
