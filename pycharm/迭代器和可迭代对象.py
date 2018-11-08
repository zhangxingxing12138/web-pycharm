from collections import Iterable
class MyList(object):
    def __init__(self):
        self.items = []

    def add(self, val):
        self.items.append(val)

    def __iter__(self):#加这个方法变成了可迭代对象（iterable）
        myiterator = MyIterator(self)
        return myiterator#返回一个迭代器(MyIterator(self))


class MyIterator(object):
    def __init__(self, mylist):
        self.mylist = mylist
        self.current = 0
#iter(可迭代对象)可以将可迭代对象转换成迭代器
    def __next__(self):#有next方法的成为迭代器  for 循环取值调用next方法
        if self.current < len(self.mylist.items):
            item = self.mylist.items[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


mylist = MyList()
mylist.add('老王')
mylist.add('老张')
mylist.add('老宋')

for num in mylist:
    print(num)