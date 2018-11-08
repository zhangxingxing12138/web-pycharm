#生成器方法1：把列表生成式的 [ ] 改成 ( )
def fib():#方法2
    a, b = 0, 1
    for i in range(20):
        # print(a)
        # print('22222222222')
        v=yield a#不管yield在哪只要有这个函数就是生成器
        print(v+'wang')
        # print('44444444444')
        a,b=b,b+a
# fib()
f=fib()
print(next(f))#停在了yield上面
# f.send('lso')#也可以唤醒 ,send中必须传参数，可以传None

# print(next(f))#在调用一次再执行yeild下面的代码，然后遇到yeild在停
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(f)
# while True:
#     try:
#         print(next(f))
#     except StopIteration as e:
#         break























