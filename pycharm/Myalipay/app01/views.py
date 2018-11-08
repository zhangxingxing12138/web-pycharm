from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from utils.pay import AliPay
import time
from django.conf import settings


def aliPay():
    obj = AliPay(
        appid=settings.APPID,
        app_notify_url=settings.NOTIFY_URL,
        return_url=settings.RETURN_URL,
        alipay_public_key_path=settings.PUB_KEY_PATH,
        app_private_key_path=settings.PRI_KEY_PATH,
        debug=True,  # 默认False,
    )
    return obj


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    alipay = aliPay()

    money = float(request.POST.get('price'))
    out_trade_no = "x2" + str(time.time())

    query_params = alipay.direct_pay(
        subject="苹果",
        out_trade_no=out_trade_no,
        total_amount=money,
    )

    pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)

    return redirect(pay_url)


def pay_result(request):
    params = request.GET.dict()
    sign = params.pop('sign', None)

    alipay = aliPay()

    status = alipay.verify(params, sign)

    if status:
        return HttpResponse('支付成功')
    return HttpResponse('支付失败')


@csrf_exempt
def update_order(request):
    if request.method == 'POST':
        from urllib.parse import parse_qs

        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)

        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]

        alipay = aliPay()

        sign = post_dict.pop('sign', None)
        status = alipay.verify(post_dict, sign)
        if status:
            out_trade_no = post_dict.get('out_trade_no')
            print(out_trade_no)
            return HttpResponse('支付成功')
        else:
            return HttpResponse('支付失败')
    return HttpResponse('')
