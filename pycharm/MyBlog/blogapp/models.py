from django.db import models
from userapp.models import BlogUser


# Create your models here.

# 轮播图
class Banner(models.Model):
    title = models.CharField(verbose_name='标题', max_length=20)
    cover = models.ImageField('封面', upload_to='static/imgs/banner')
    link_url = models.URLField('链接', max_length=256)
    idx = models.IntegerField('索引')
    is_active = models.BooleanField('是否被激活', default=False)

    def __str__(self):
        return self.title

    class Meta:  # 元选项
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


# 分类字段
class Category(models.Model):
    name = models.CharField('名字', max_length=20)

    def __str__(self):
        return self.name

    class Meta:  # 元选项
        verbose_name = '分类'
        verbose_name_plural = verbose_name


# 标签
class Tags(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:  # 元选项
        verbose_name = '标签'
        verbose_name_plural = verbose_name


# 文章类
class Post(models.Model):
    user = models.ForeignKey(BlogUser,verbose_name='作者')
    category = models.ForeignKey(Category,verbose_name='分类')
    tags = models.ManyToManyField(Tags,verbose_name='标签')
    title = models.CharField(max_length=50,verbose_name='标题')
    cover = models.ImageField(upload_to='static/imgs/post',verbose_name='封面')
    pub_date = models.DateTimeField('发布日期')
    views = models.IntegerField(default=0,verbose_name='浏览量')
    content = models.TextField(verbose_name='内容')
    recommend = models.BooleanField(default=False,verbose_name='推荐')

    def __str__(self):
        return self.title

    class Meta:  # 元选项
        verbose_name = '文章'
        verbose_name_plural = verbose_name


# 友情链接
class Link(models.Model):
    name = models.CharField(max_length=20,verbose_name='名字')
    link_url = models.URLField(max_length=256, default='',verbose_name='链接')

    def __str__(self):
        return self.name

    class Meta:  # 元选项
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name


# 评论内容
class Comment(models.Model):
    user = models.ForeignKey(BlogUser,verbose_name='用户')
    post = models.ForeignKey(Post,verbose_name='文章')
    content = models.CharField(max_length=256,verbose_name='内容')
    comment_date = models.DateTimeField(verbose_name='评论日期')

    def __str__(self):
        return self.content

    class Meta:  # 元选项
        verbose_name = '评论'
        verbose_name_plural = verbose_name
