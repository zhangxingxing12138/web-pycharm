from django.db import models
from tinymce.models import HTMLField

from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(verbose_name='标题', max_length=20, db_column='title')
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    hcomment = models.CharField(max_length=200)
    isDelete = models.BooleanField(default=False)
    hbook = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname

    def gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'

    gender.admin_order_field = 'id'  # 排序
    gender.short_description = '性别'

    def name(self):
        return self.hname

    name.short_description = '姓名'

    def parent(self):
        return self.hbook

    parent.short_description = '父级区域名称'

    class Meta:
        db_table = 'heroinfo'


class PicTest(models.Model):
    pic = models.ImageField(upload_to='booktest/')


class AreaInfo(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', blank=True, null=True)


class GoodsInfo(models.Model):
    gcontent = HTMLField()  # 描述信息


class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = RichTextUploadingField()
