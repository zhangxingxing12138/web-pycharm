import time
from celery import task
from django.core.mail import *
from django.conf import settings


@task
def sayHello():
    msg = '请点击下面的链接重置密码: http://127.0.0.1:8000/reset/3123312'
    send_mail('注册激活', msg, settings.EMAIL_FROM,
              ['496155678@qq.com'])
