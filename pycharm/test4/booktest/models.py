from django.db import models


# Create your models here.
# 书类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle

    def btitle1(self):
        return '老王'


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    hbook = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname


class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parea = models.ForeignKey('self', blank=True, null=True)


class PicTest(models.Model):
    pic = models.ImageField(upload_to='static/imgs')
