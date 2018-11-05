from multiprocessing import Pool
import time
def test():
    for i in range(5):
        time.sleep(0.5)
        print('做饭中')
    return '饭做好了'
def test2(msg):
    print(msg)
p=Pool()
p.apply_async(func=test,callback=test2)
for i in range(10):
    print('做作业')
    time.sleep(0.5)
