from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^upload/$', views.upload),
    url(r'^page_text/(\d*)$', views.page_text),
    url(r'^index3/$', views.index3),
    url(r'^pro/$', views.pro),
    url(r'^city/(\d+)/$', views.city),
    url(r'^index4/', views.index4),
    url(r'^editor/', views.editor),
    url(r'^submit_content', views.submit_content),
    url(r'^index5', views.ck),
    url(r'^query/', views.query),
    url(r'^index6/', views.index6),
    url(r'^send/', views.send),
    url(r'^index7/', views.index7),
    url(r'^index8/', views.index8),

]

# site_packages---tinymce---static---tinymce
#
#
# langs
# themes
# tiny_mce_src.js
