# from multiprocessing import Process
# import time
# class process_zxx(Process):
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         for i in range(5):
#             time.sleep(1)
#             print('哈哈')
# p=process_zxx()
#
# p.start()
# p.join(3)
# print('嘻嘻')


# 进程池创建进程
# from multiprocessing import Pool
# import time
# def work():
#     for i in range(5):
#         time.sleep(1)
#         print('老王')
# p = Pool(2)
# for i in range(3):
#     # p.apply_async(work)
#     p.apply(work)
#     print('添加成功')
# p.close()
# p.join()
#




from multiprocessing import Manager,Pool
import time

def write(q):
    for i in range(10):
        time.sleep(0.5)
        print('添加成功')
        q.put(i)
def read(q):
    while True:
        if q.qsize()>0:
            num = q.get()
            print(num)
            if num==9:
                break
p = Pool()
q=Manager().Queue()
p.apply_async(write,(q,))
p.apply_async(read,(q,))

p.close()
p.join()

