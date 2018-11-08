from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^$', views.Index.as_view()),
    url(r'^index2/$', views.index2),
    url(r'^login/$', views.login),
    url(r'^loginhandle/$', views.loginhandle),
    url(r'^loginout/$', views.loginout),
    url(r'^index3/$', views.index3,name='index3'),

]
