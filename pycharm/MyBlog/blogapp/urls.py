from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^list/$', views.post_list),
    url(r'^search/$', views.search),
    url(r'^index/$', views.index),
    url(r'^show/(?P<pid>\d+)$', views.show),
    url(r'^category/(?P<cid>\d+)/$', views.post_list),
    url(r'^tags/(?P<tid>\d+)/$', views.post_list),
    url(r'^comment/(?P<pid>\d+)/', views.comment),
    url(r'^register/', views.register),
    url(r'^login/', views.loginin),
    url(r'^active/(?P<active_code>[a-zA-Z0-9]+)', views.active),
    url(r'^reset/(?P<active_code>[a-zA-Z0-9]+)', views.reset),
    url(r'^loginout/', views.loginout),
    url(r'^forget/', views.forget),
    url(r'^newpwd/', views.newpwd),

]
