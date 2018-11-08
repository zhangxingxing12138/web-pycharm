from django.shortcuts import render
from .models import *
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.
# 变量
def index(request):
    b = BookInfo.objects.get(pk=1)
    ctx = {
        'b': b
    }
    return render(request, 'booktest/index.html', ctx)


# 标签
def index2(request):
    list = BookInfo.objects.all()
    # list = None
    ctx = {
        'list': list
    }
    return render(request, 'booktest/index2.html', ctx)


# 过滤器
def index3(request):
    list = BookInfo.objects.all()
    # list = None
    ctx = {
        'list': list,
        'data': '隔壁老王'
    }
    return render(request, 'booktest/index3.html', ctx)


def index4(request):
    return render(request, 'booktest/index4.html')


def index5(request):
    return render(request, 'booktest/index5.html')


def user1(request):
    return render(request, 'booktest/user1.html')


def user2(request):
    return render(request, 'booktest/user2.html')


# 转义
def index6(request):
    ctx = {
        'ctx': '<h1>哈哈</h1>'
    }
    return render(request, 'booktest/index6.html', ctx)


def csrf1(request):
    return render(request, 'booktest/csrf1.html')


def csrf2(request):
    name = request.POST.get('name')
    ctx = {
        'name': name
    }
    return render(request, 'booktest/csrf2.html', ctx)


def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # rand_str = '1234'
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('/System/Library/Fonts/Keyboard.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def index7(request):
    return render(request, 'booktest/index7.html')


# 验证
def check_code(request):
    code = request.POST.get('code').lower()
    code1 = request.session.get('verifycode').lower()
    if code == code1:
        return HttpResponse('验证成功')
    else:
        return HttpResponse('验证失败')


def index8(request):
    return render(request, 'booktest/index8.html')


# 反向解析
def fan1(request):
    return HttpResponse('fan1')


def fan2(request):
    return HttpResponse('fan2')


def fan3(request, id, id1):
    return HttpResponse(id + id1)


def fan4(request, id, id1):
    return HttpResponse(id + id1)


# 重定向反向解析
def fan5(request):
    return redirect(reverse('booktest:fan2'))


def fan6(request, id3, id4):
    return HttpResponseRedirect(reverse('booktest:fan3', args=(id3, id4)))


def fan7(request, id5, id6):
    return redirect(reverse('booktest:fan4', kwargs={"id": id5, 'id1': id6}))


# 静态文件

def index9(request):
    return render(request, 'booktest/index9.html')


# 中间件

def index10(request):
    # print("我在中间件后面执行")
    print(a)
    return render(request, 'booktest/index10.html')
