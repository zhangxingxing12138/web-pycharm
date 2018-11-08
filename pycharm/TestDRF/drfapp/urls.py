from django.conf.urls import url, include
from . import views

from rest_framework.routers import DefaultRouter

# from .views import *
from rest_framework.documentation import include_docs_urls

#
# book_list = views.BookViewSet.as_view(
#     {
#         'get': 'list',
#         'post': 'create'
#     }
# )
#
# book_detail = views.BookViewSet.as_view(
#     {
#         'get': 'retrieve',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destory'
#     }
# )

# 创建一个路由
router = DefaultRouter()
#
router.register(r'books', views.BookViewSet)
router.register(r'publisher', views.PublisherViewSet)

urlpatterns = [
    # url(r'^$', views.api_root),
    url(r'^', include(router.urls)),
    url(r'^docs/', include_docs_urls(title='图书管理系统')),
    # url(r'publisher_list/$', views.publisher_list.as_view(), name='publisher_list'),
    # url(r'publisher/(?P<pk>\d+)/$', views.publisher_detail.as_view(), name='publisher-detail'),
    # url(r'book_list/$', views.book_list.as_view(), name='book_list'),
    # url(r'book/(?P<pk>\d+)/$', views.book_detail.as_view(), name='book-detail')

    # url(r'^books/$', book_list, name='book_list'),
    # url(r'^books/(?P<pk>[0-9])/$', book_detail, name='book_detail')
]
