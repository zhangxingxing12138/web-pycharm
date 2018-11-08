from collections import Iterable
class MyList(object):
    def __init__(self):
        self.items = []
        self.index = 0


    def add(self, name):
        self.items.append(name)
        self.index = 0
    def __iter__(self):#加这个方法变成了可迭代对象（iterable）
        return self  #返回一个迭代器(MyIterator(self))
    def __next__(self):#有next方法的成为迭代器  for 循环取值调用next方法
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration



mylist = MyList()
mylist.add('老王')
mylist.add('老张')
mylist.add('老宋')

for num in mylist:
    print(num)