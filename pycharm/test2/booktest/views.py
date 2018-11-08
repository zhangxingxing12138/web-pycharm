from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.db.models import F, Q, Sum


# Create your views here.

def index(request):
    list = BookInfo.objects.all()
    ctx = {
        'list': list
    }

    return render(request, 'booktest/index.html', ctx)


def create(request):
    b = BookInfo()
    b.btitle = "红楼梦"
    b.bread = 1000
    b.bpub_date = datetime.now()
    b.bcomment = 0
    b.save()
    return redirect('/')


def delete(request, bid):
    b = BookInfo.objects.filter(pk=bid)
    b.delete()
    return redirect('/')


def show(request):
    # list = BookInfo.objects.filter(btitle__contains='龙')
    # list = BookInfo.objects.filter(btitle__isnull=False)
    # list = BookInfo.objects.filter(id__in=[1, 3, 4])
    # list = BookInfo.objects.filter(id__lte=3)
    # list = BookInfo.objects.exclude(id=1)
    # list = BookInfo.objects.filter(bpub_date__year=1980)

    # list = BookInfo.objects.filter(bread__gte=F('bcomment'))
    list = BookInfo.objects.filter(Q(bread__gt=20) | Q(pk__lt=3))
    # list = BookInfo.objects.filter(bread__gt=20).filter(pk__lt=3)
    reads = BookInfo.objects.aggregate(Sum('bread'))
    count = BookInfo.objects.count()
    print(reads)
    ctx = {
        'list': list,
        'count': count,

    }

    #一查多
    b = BookInfo.objects.get(id=1)
    b.heroinfo_set.all()
    #多查一
    h = HeroInfo.objects.get(id=1)
    h.hbook
    return render(request, 'booktest/show.html', ctx)
