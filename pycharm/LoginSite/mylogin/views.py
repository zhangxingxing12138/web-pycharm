from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from .forms import *
import hashlib


# Create your views here.


def mymd5(data):
    return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()


def index(request):
    username = request.session.get('username')
    is_login = request.session.get('is_login', False)
    return render(request, 'index.html', locals())


def login(request):
    # 不允许重复登录
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写内容'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == mymd5(password):
                    # 通过下面三句话　往session字典里面写入用户状态和数据
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['username'] = user.name
                    return redirect('/index/')
                else:
                    message = '密码不正确'
            except:
                message = '用户不存在'
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())


def register(request):
    # 不允许重复登录
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']

            if password1 != password2:
                message = '两次输入密码不一样'
                return render(request, 'register.html', locals())

            user_name = User.objects.filter(name=username)
            if user_name:
                message = '用户名已经存在'
                return render(request, 'register.html', locals())

            user_email = User.objects.filter(email=email)
            if user_email:
                message = '邮箱已经存在'
                return render(request, 'register.html', locals())

            user = User()
            user.name = username
            user.email = email
            user.password = mymd5(password1)
            user.sex = sex
            user.save()
            return redirect('/login/')

    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def logout(request):
    del request.session['is_login']
    del request.session['username']
    return redirect('/index/')
