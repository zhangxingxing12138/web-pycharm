# from gevent import monkey
# import gevent
# import urllib.request
#
# # 有耗时操作时需要
# monkey.patch_all()
#
# def my_downLoad(url):
#     print('GET: %s' % url)
#     resp = urllib.request.urlopen(url)
#     data = resp.read()
#     print('%d bytes received from %s.' % (len(data), url))
#
# gevent.joinall([
#         gevent.spawn(my_downLoad, 'http://www.baidu.com/'),
#         gevent.spawn(my_downLoad, 'http://www.sina.cn/'),
#         gevent.spawn(my_downLoad, 'http://www.163.com/'),
# ])
from gevent import monkey
import gevent
import urllib.request

#有IO才做时需要这一句
monkey.patch_all()

def my_downLoad(file_name, url):
    # print('GET: %s' % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()

    with open(file_name, "wb") as f:
        f.write(data)

    # print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(my_downLoad, "1.png", 'http://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=%E5%9B%BE%E7%89%87&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&cs=2486956696,687545127&os=4287098919,2858660593&simid=0,0&pn=0&rn=1&di=147063396590&ln=1712&fr=&fmq=1541569863865_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F01d881579dc3620000018c1b430c4b.JPG%403000w_1l_2o_100sh.jpg&rpstart=0&rpnum=0&adpicid=0'),
        gevent.spawn(my_downLoad, "2.png", 'http://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=%E5%9B%BE%E7%89%87&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&cs=2486956696,687545127&os=4287098919,2858660593&simid=0,0&pn=0&rn=1&di=147063396590&ln=1712&fr=&fmq=1541569863865_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F01d881579dc3620000018c1b430c4b.JPG%403000w_1l_2o_100sh.jpg&rpstart=0&rpnum=0&adpicid=0'),
])