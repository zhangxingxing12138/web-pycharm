from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^show(\d+)/$', views.show),
    url(r'^show(?P<bid>\d+)/$', views.show),
    url(r'^showtest/$', views.show1),
    url(r'^gettest/$', views.gettest),
    url(r'^posttest/$', views.posttest),
    url(r'^getorpost/$', views.getorpost),
    url(r'^setcookie/$', views.set_cookie),
    url(r'^getcookie/$', views.get_cookie),
    url(r'^delcookie/$', views.del_cookie),
    url(r'^login/$', views.login),
    url(r'^loginshow/$', views.loginshow),
    url(r'^login_handle/$', views.loginhandle),
    url(r'^login_out/$', views.loginout),

]
