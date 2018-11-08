import hashlib
from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.

def index(request):
    return render(request, 'index.html')


# def login(request):
#     if request.method == 'POST':
#         msg = "所有字段必须填写"
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             user = User.objects.get(name=username)
#         except:
#             msg = "用户不存在"
#             return render(request, 'login.html', {"msg": msg})
#         if user.password == password:
#             return redirect("/index/")
#         else:
#             msg = "密码不正确"
#     return render(request, 'login.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    login_form = UserForm(request.POST)
    # 使用表单类自带的is_valid()方法一步完成数据验证工作；
    if login_form.is_valid():

        # 验证成功后可以从表单对象的cleaned_data数据字典中获取表单的具体值；
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']

        print(username, password)
        message = '所有字段都必须填写'

        if username and password:  # 确保用户名和密码都不为空
            # 通过strip()方法，将用户名前后无效的空格剪除；
            username = username.strip()
            # 用户名字符合法验证
            # 密码长度验证
            # 更多其他验证

            try:
                user = User.objects.get(name=username)
                if user.password == hash_code(password):
                    # 通过下面三句话　往session字典里面写入用户状态和数据
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = '密码不正确'
            except:
                message = '用户名不存在'

        return render(request, 'login.html', locals())
        # 另外，这里使用了一个小技巧，Python内置了一个locals()函数，它返回当前所有的本地变量字典，我们可以偷懒的将这作为render函数的数据字典参数值，就不用费劲去构造一个形如{'message':message, 'login_form':login_form}的字典了。这样做的好处当然是大大方便了我们，但是同时也可能往模板传入了一些多余的变量数据，造成数据冗余降低效率。

    else:
        login_form = UserForm()
        return render(request, 'login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def logout(request):
    """退出登录后重定向到首页"""
    if not request.session.get('is_login', None):
        # 如果本来就未登录,也就没有登出一说
        return redirect('/index/')
    request.session.flush()
    return redirect("/index/")


def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()
