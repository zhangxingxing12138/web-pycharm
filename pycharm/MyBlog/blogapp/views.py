from django.shortcuts import render

from .models import *

from django.db.models import Q

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth import authenticate, login, logout

from userapp.models import EmailVerifyRecord

from random import Random
from django.core.mail import send_mail
from MyBlog.settings import EMAIL_FROM


# Create your views here.


def index(request):
    banner_list = Banner.objects.all()  # 轮播图数据
    post_list = Post.objects.filter(recommend=True).all()[:1]  # 推荐数据
    category_list = Category.objects.all()  # 分类
    new_post_list = Post.objects.order_by('-pub_date').all()  # 最新发布
    new_comment_list = Comment.objects.order_by('-comment_date').all()  # 取最新评论
    friend_list = Link.objects.all()
    post_ids = []  # 装文章id
    comment_list = []  # 过滤后的评论

    for comment in new_comment_list:  # 过滤重复的数据
        if comment.post.id not in post_ids:
            post_ids.append(comment.post.id)
            comment_list.append(comment)

    ctx = {
        'banner_list': banner_list,
        'post_list': post_list,
        'category_list': category_list,
        'new_post_list': new_post_list,
        'comment_list': comment_list,
        'friend_list': friend_list,
    }
    return render(request, 'index.html', ctx)


# 列表页
def post_list(request, cid=-1, tid=-1):
    if cid != -1:  # 传分类id
        category = Category.objects.get(pk=cid)
        post_all_list = category.post_set.all()
    elif tid != -1:  # 传标签id
        tag = Tags.objects.get(pk=tid)
        post_all_list = tag.post_set.all()
    else:  # 不传分类id和不传标签id就找全部
        post_all_list = Post.objects.all()  # 找出所有博客
    new_comment_list = Comment.objects.order_by('-comment_date').all()  # 取最新评论

    tag_list = Tags.objects.all()  # 取所有标签
    post_ids = []  # 装文章id
    comment_list = []  # 过滤后的评论

    for comment in new_comment_list:  # 过滤重复的数据
        if comment.post.id not in post_ids:
            post_ids.append(comment.post.id)
            comment_list.append(comment)

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(post_all_list, per_page=1, request=request)

    post_all_list = p.page(page)

    ctx = {
        'post_all_list': post_all_list,
        'comment_list': comment_list,
        'tag_list': tag_list

    }
    return render(request, 'list.html', ctx)


# 搜索
def search(request):
    kw = request.GET.get('keyword', '')
    tag_list = Tags.objects.all()  # 取所有标签
    post_list = Post.objects.filter(Q(title__icontains=kw) | Q(content__icontains=kw))
    print(post_list)
    new_comment_list = Comment.objects.order_by('-comment_date').all()  # 取最新评论
    post_ids = []  # 装文章id
    comment_list = []  # 过滤后的评论

    for comment in new_comment_list:  # 过滤重复的数据
        if comment.post.id not in post_ids:
            post_ids.append(comment.post.id)
            comment_list.append(comment)

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(post_list, per_page=1, request=request)

    post_all_list = p.page(page)
    ctx = {
        'post_all_list': post_all_list,
        'tag_list': tag_list,
        'comment_list': comment_list,
    }
    return render(request, 'list.html', ctx)


# 详情页
def show(request, pid):
    post = Post.objects.get(pk=pid)
    comments = Comment.objects.order_by('-comment_date').all()
    tag_list = post.tags.all()  # 取出这篇文章所有标签
    post_list = []
    for tag in tag_list:
        post_list.extend(tag.post_set.all())  # 注意

    new_comment_list = Comment.objects.order_by('-comment_date').all()  # 取最新评论
    post_ids = []  # 装文章id
    comment_list = []  # 过滤后的评论

    for comment in new_comment_list:  # 过滤重复的数据
        if comment.post.id not in post_ids:
            post_ids.append(comment.post.id)
            comment_list.append(comment)
    ctx = {
        'post': post,
        'post_list': post_list,
        'comment_list': comment_list,
        'comments': comments
    }
    return render(request, 'show.html', ctx)


def comment(request, pid):
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user  # 默认user对象
        comment.post = Post.objects.get(pk=pid)
        comment.content = request.POST.get("content", "这家伙很懒")
        comment.comment_date = datetime.now()
        comment.save()
        return HttpResponseRedirect('/show/' + pid)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        email = request.POST.get('email')
        user = BlogUser.objects.filter(username=uname)
        if len(user) > 0:
            return render(request, 'register.html', {"error": "用户名以存在"})

        user = BlogUser.objects.filter(email=email)
        if len(user) > 0:
            return render(request, 'register.html', {"error": "邮箱以存在"})
        my_send_email(email)  # task任务 耗时
        user = BlogUser()
        user.username = uname
        user.password = make_password(pwd)
        user.email = email
        user.is_active = False  # 没激活
        # user.is_staff #是否可以登录管理后台
        # user.is_superuser #是否是超管
        # user.is_authenticated #是否严重
        user.save()
        return render(request, 'login.html', {"error": "已经向当前邮箱发送一封邮件"})


def loginin(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        # user = authenticate(username=uname, password=pwd)
        user = BlogUser.objects.filter(username=uname)
        if len(user) > 0:
            if user[0].is_active:
                if check_password(pwd, user[0].password):
                    login(request, user[0])
                    # #假如他没勾选自动登录
                    #     request.session.set_expiry(0)
                    return HttpResponseRedirect('/index/')
                else:
                    return render(request, 'login.html', {"error": '用户或密码错误'})
            else:
                return render(request, 'login.html', {"error": '用户没激活'})
        else:
            return render(request, 'login.html', {"error": '用户或密码错误'})


# 生成随机字符串
def make_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


# 发送邮件
def my_send_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = make_random_str(4)
    else:
        code = make_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "博客-注册激活链接"
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "博客-网注册密码重置链接"
        email_body = "请点击下面的链接重置密码: http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "博客-邮箱修改验证码"
        email_body = "你的邮箱验证码为: {0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


# 验证
def active(request, active_code):
    ## filter 返回的能遍历的列表
    ## get 一般返回一个对象 不需要遍历
    all_records = EmailVerifyRecord.objects.filter(code=active_code)
    if all_records:
        for record in all_records:
            if record.send_type == 'register':
                email = record.email
                user = BlogUser.objects.get(email=email)
                user.is_active = True
                user.save()
                record.delete()
            elif record.send_type == 'forget':
                request.session['email'] = email
                record.delete()
                return render(request, 'newpwd.html')
    else:
        return HttpResponse("验证失败")
    return render(request, "login.html")


def reset(request, active_code):
    all_records = EmailVerifyRecord.objects.filter(code=active_code)
    if all_records:
        for record in all_records:
            email = record.email
            request.session['email'] = email
            # record.delete()
            return render(request, 'newpwd.html')
    else:
        return HttpResponse("验证失败")
    return render(request, "login.html")


def loginout(request):
    logout(request)
    return HttpResponseRedirect('/index/')


def forget(request):
    if request.method == 'GET':
        return render(request, "forpwd.html")
    else:
        email = request.POST.get('email')
        user = BlogUser.objects.filter(email=email)
        if len(user) == 0:
            return render(request, 'register.html', {"error": "邮箱未注册"})
        else:
            my_send_email(email, send_type="forget")
            return render(request, 'forpwd.html', {"error": "邮箱已发送"})


def newpwd(request):
    if request.method == 'POST':
        pwd1, pwd2 = request.POST.getlist('password')
        if pwd1 != pwd2:
            return render(request, "newpwd.html", {"error": "密码不一样"})
        else:
            email = request.session.get('email')
            user = BlogUser.objects.get(email=email)
            user.set_password(pwd1)
            user.save()
            request.session.flush()

            return HttpResponseRedirect('/login/')
