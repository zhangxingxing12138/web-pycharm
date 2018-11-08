from django.db import models


# Create your models here.
# 把数据----序列化成可以储存到磁盘的过程

#出版社
class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name='出版社', unique=True)
    address = models.CharField(max_length=256, verbose_name='地址')
    operator = models.ForeignKey('auth.User')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

class Book(models.Model):
    name = models.CharField(max_length=32,verbose_name='书')
    publisher = models.ForeignKey(Publisher)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

