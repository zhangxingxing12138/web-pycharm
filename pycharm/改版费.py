class MyList(object):
    def __init__(self,num):

        self.index = 0
        self.num=num
        self.a=0
        self.b = 1


    def __iter__(self):#加这个方法变成了可迭代对象（iterable）
        return self  #返回一个迭代器(MyIterator(self))
    def __next__(self):#有next方法的成为迭代器  for 循环取值调用next方法

        if self.index < self.num:
            a=self.a
            self.a,self.b=self.b,self.a+self.b
            self.index += 1

            return a
        else:
            raise StopIteration



mylist = MyList(2)


for num in mylist:
    print(num)