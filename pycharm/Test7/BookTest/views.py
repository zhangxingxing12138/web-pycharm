from django.shortcuts import render
from .models import *
from django.views.generic.base import View
from django.http import HttpResponseRedirect


# Create your views here.

# 用函数的方式
def index(request):
    books = BookInfo.objects.all()
    ctx = {
        'books': books
    }
    return render(request, 'booktest/index.html', ctx)


# 用类的方式做
class Index(View):

    def get(self, request):
        books = BookInfo.objects.all()
        ctx = {
            'books': books
        }
        return render(request, 'booktest/index.html', ctx)

    def post(self, request):
        pass


def index2(request):
    name = request.session.get('myname', 1)
    ctx = {
        'name': name

    }
    return render(request, 'booktest/index2.html', ctx)


def login(request):
    return render(request, 'booktest/login.html')


def loginhandle(request):
    name = request.POST.get('name')
    request.session['myname'] = name
    request.session.set_expiry(5)  # 设置过期时间
    return HttpResponseRedirect("/index2/")


def loginout(request):
    del request.session['myname']
    return HttpResponseRedirect("/index2/")


def index3(request):
    ctx = {
        'list': range(10)
    }
    return render(request, 'booktest/index3.html', ctx)
