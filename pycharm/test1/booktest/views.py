from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *


# Create your views here.
# render 渲染
# loader 加载
# get_template 得到模板
def index(request):
    # 获取数据
    list = BookInfo.objects.all()
    # 加载模板
    template = loader.get_template('booktest/index.html')
    # template
    ctx = {
        'list': list
    }
    # 返回并渲染模板
    return HttpResponse(template.render(ctx))


def show(request, bid):
    book = BookInfo.objects.get(id=bid)
    list = book.heroinfo_set.all()
    ctx = {
        'list': list
    }
    return render(request, 'booktest/show.html', ctx)
