from django.shortcuts import render
from utils.pay import AliPay
import time
from django.shortcuts import redirect
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


# Create your views here.
def getobj():
    obj = AliPay(
        appid= settings.APPID,
        app_notify_url='http://47.93.220.42:80/update/',  # post请求
        return_url='httppycryptodome://47.93.220.42:80/result/',  # 支付完跳转的地址
        alipay_public_key_path='keys/alipay_public_2048.txt',
        app_private_key_path='keys/app_private_2048.txt',
        debug=True,  # 默认False,
    )

    return obj


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:

        obj = getobj()

        money = float(request.POST.get('price'))
        out_trade_no = "x2" + str(time.time())  # 订单号
        # 订单状态 待支付
        query_params = obj.direct_pay(
            subject="苹果",  # 商品描述
            out_trade_no=out_trade_no,  # 订单号
            total_amount=money,  # 商品价格 保留两位小数
        )

        pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)

        return redirect(pay_url)


def result(request):
    params = request.GET.dict()
    sign = params.pop('sign', None)

    obj = getobj()
    status = obj.verify(params, sign)

    if status:
        return HttpResponse('支付成功')
    return HttpResponse('支付失败')


@csrf_exempt
def update(request):
    '''

    假设找到订单-----把订单已支付
    :param request:
    :return:
    '''

    if request.method == 'POST':
        from urllib.parse import parse_qs

        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)

        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]

        obj = getobj()
        sign = post_dict.pop('sign', None)
        print(sign)
        status = obj.verify(post_dict, sign)
        if status:
            out_trade_no = post_dict.get('out_trade_no')
            print(out_trade_no)
            return HttpResponse('支付成功')
        else:
            return HttpResponse('支付失败')
    return HttpResponse('')
