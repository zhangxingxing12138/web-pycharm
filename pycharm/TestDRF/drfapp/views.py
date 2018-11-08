from django.shortcuts import render
from .models import Publisher, Book
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
import json
from . import serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication
from rest_framework.views import APIView
from django.http import Http404

from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from .MyPermission import IsOwnerOrReadOnly

from rest_framework.reverse import reverse

from rest_framework import viewsets


# Create your views here.


# def publishers(request):
# pub_list = Publisher.objects.all()
# pub_list = Publisher.objects.all().values()
# print(pub_list)
# 第一种办法 序列化json数据
# l = []
# for pub in pub_list:
#     d = {}
#     d['name'] = pub.name
#     d['address'] = pub.address
#     l.append(d)

# 这是第二种方案
# for pub in pub_list:
#     l.append(model_to_dict(pub))
# 第三种方案
# data = serializers.serialize('json', pub_list)

# 这是DRF提供的序列化
# p = Publisher.objects.all()
# d = serializer.PublisherSerializers(p, many=True)
# return HttpResponse(json.dumps(d.data), content_type='application/json')
# return JsonResponse(list(pub_list), safe=False


# @api_view(['GET', 'POST'])
# def publisher_list(request):
#     if request.method == 'GET':
#         queryset = Publisher.objects.all()
#         s = serializer.PublisherSerializers(queryset, many=True)
#         return Response(s.data)
#     elif request.method == 'POST':
#         s = serializer.PublisherSerializers(data=request.data)
#         if s.is_valid():  # 检验数据是否正确
#             s.save()
#             return Response(s.data)
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def publisher_detail(request, pk):
#     try:
#         p = Publisher.objects.get(pk=pk)
#     except p.DoesNotExist:
#         return Response(status.HTTP_204_NO_CONTENT)
#
#     if request.method == 'GET':  # 获取单条数据
#         p = serializer.PublisherSerializers(p)
#         return Response(p.data)
#
#     elif request.method == 'PUT':  # 更新
#         p = serializer.PublisherSerializers(p, data=request.data)
#         if p.is_valid():
#             p.save()
#             return Response(p.data)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':  # 删除
#         p.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class publisher_list(APIView):
#     def get(self, request):
#         queryset = Publisher.objects.all()
#         s = serializer.PublisherSerializers(queryset, many=True)
#         return Response(s.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         s = serializer.PublisherSerializers(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data)
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class publisher_detail(APIView):
#     def get_object(self, pk):  # 查单个
#         try:
#             p = Publisher.objects.get(pk=pk)
#             return p
#         except Publisher.DoesNotExist:
#             raise Http404  # 抛出异常
#
#     def get(self, request, pk):
#         p = self.get_object(pk)
#         s = serializer.PublisherSerializers(p)
#         return Response(s.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         p = self.get_object(pk)
#         s = serializer.PublisherSerializers(p, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_200_OK)
#         else:
#
#             return Response(s.errors, status=status.HTTP_404_NOT_FOUND)
#
#     def delete(self, request, pk):
#         p = self.get_object(pk=pk)
#         p.delete()  # 物理性删除
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class publisher_list(mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      generics.GenericAPIView):
#     queryset = Publisher.objects.all()#给指定集合
#     serializer_class = serializer.PublisherSerializers#指定序列化类
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class publisher_detail(mixins.UpdateModelMixin,
#                        mixins.RetrieveModelMixin,
#                        mixins.DestroyModelMixin,
#                        generics.GenericAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = serializer.PublisherSerializers
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# 最后api了
# 出版社
# class publisher_list(generics.ListCreateAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = serializer.PublisherSerializers
#     permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
#
#     def perform_create(self, serializer):  # 重写这个方法
#         serializer.save(operator=self.request.user)
#
#
# class publisher_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = serializer.PublisherSerializers
#     permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)


# # 书
# class book_list(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = serializer.BookSerializers
#
#
# class book_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = serializer.BookSerializers


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializer.BookSerializers


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = serializer.PublisherSerializers

# 预览api
@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'publishers': reverse('publisher_list', request=request, format=format),
            'books': reverse('book_list', request=request, format=format)
        }
    )
