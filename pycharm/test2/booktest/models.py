from django.db import models
from datetime import datetime


# Create your models here.

# 自定义管理器
class Book2(models.Manager):
    pass

    def all(self):
        return super().all().filter(isDelete=False)

    def create(self, name):
        b = BookInfo()
        b.btitle = name
        b.bpub_date = datetime.now()
        b.save()

    def show(self):
        return '哈哈'


# 书类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle

    # 自定义管理器
    book1 = models.Manager()
    book2 = Book2()

    #'booktest_bookinfo'
    class Meta:
        db_table = 'bookinfo'


    '''
    @classmethod
    def create(cls, name):
        b = BookInfo()
        b.btitle = name
        b.bpub_date = datetime.now()
        b.save()
    '''

'''
默认管理器 ------ objects
作用：模型和数据库交互

提供的方法不能满足一些需求

all()
filter()
get()





'''



# 英雄类


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    hbook = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname
