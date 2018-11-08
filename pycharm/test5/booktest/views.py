from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *
from django.http import JsonResponse
import json
from .tasks import sayHello
import time
from django.core.mail import *
from celery import task
from django.views.decorators.cache import cache_page


# Create your views here.


def index(request):
    return render(request, 'booktest/index.html')


def upload(request):
    f1 = request.FILES.get('pic')
    '''
    七牛云
    
    '''

    filename = '%s/booktest/%s' % (settings.MEDIA_ROOT, f1.name)

    with open(filename, 'wb') as pic:
        for c in f1.chunks():  # 分片写入
            pic.write(c)

    return HttpResponse("<img src='http://pcxfnejm2.bkt.clouddn.com/Fg0Fox9NjSZLUxnKyJVp1aQaTVz0'>")  # 把图片返回


def page_text(request, index):
    list = HeroInfo.objects.all()  # 惰性执行
    # print(list)
    paginator = Paginator(list, 3)
    if index == '':
        index = 1
    hero_list = paginator.page(int(index))
    # print(hero_list.object_list)
    ctx = {
        'hero_list': hero_list,

    }
    return render(request, 'booktest/index1.html', ctx)


def index3(request):
    return render(request, 'booktest/index3.html')


def pro(request):
    pros = AreaInfo.objects.filter(parent__isnull=True).values()
    return JsonResponse({'data': list(pros)})
    # return render(request, 'booktest/index3.html')


# JSONView
def city(request, pid):
    citys = AreaInfo.objects.filter(parent_id=pid).values()
    return HttpResponse(json.dumps({"data": list(citys)}), 'application/json')


# 富文本

def index4(request):
    list = GoodsInfo.objects.all()
    ctx = {
        'list': list
    }
    return render(request, 'booktest/index4.html', ctx)


def editor(request):
    return render(request, 'booktest/editor.html')


def submit_content(request):
    '''
    处理逻辑 保存数据
    :param request:
    :return:
    '''
    content = request.POST.get('gcontent')
    g = GoodsInfo()
    g.gcontent = content
    g.save()
    return HttpResponse('ok')


def ck(request):
    list = Blog.objects.all()
    ctx = {
        'list': list
    }
    return render(request, 'booktest/index5.html', ctx)


def query(request):
    return render(request, 'booktest/query.html')


def index6(request):
    # sayHello()
    # sayHello.delay()#另开启一个进程去执行
    print("hello")
    time.sleep(10)
    print('world')
    return HttpResponse('ok')


# pip install celery-with-redis


def send(request):
    sayHello.delay()
    return HttpResponse('ok')


@cache_page(60 * 10)
def index7(request):
    return HttpResponse("2")


def index8(request):
    return render(request, 'booktest/index8.html')
