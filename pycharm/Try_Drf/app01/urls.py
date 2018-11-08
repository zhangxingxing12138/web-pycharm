from django.conf.urls import url, include
from . import views

from rest_framework.routers import DefaultRouter

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
#         'delete': 'destroy'
#     }
# )

router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'publishers', views.PublisherViewSet)
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include_docs_urls(title='图书管理系统')),
    # url(r'^api/$', views.api_root),
    # url(r'^publishers/$', views.PublisherList.as_view(), name='publisher_list'),
    # url(r'^publishers/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view(), name='publisher_detail'),
    # url(r'^books/$', views.BooxkList.as_view(), name='book_list'),
    # url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(), name='book_detail')
    # url(r'^books/$', book_list, name='book_list'),
    # url(r'^books/(?P<pk>[0-9])/$', book_detail, name='book_detail')

]
