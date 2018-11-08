from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import json
from django.forms.models import model_to_dict
from django.core import serializers
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets


# Create your views here.

# def publisher_list(request):
# queryset = Publisher.objects.all().values()
# queryset = Publisher.objects.all()
# data = []
# for i in queryset:
#     p_tmp = {
#         'name': i.name,
#         'address': i.address
#     }
#     data.append(p_tmp)

# for i in queryset:
#     data.append(model_to_dict(i))

# data = serializers.serialize('json', queryset)

# ser = serializers.PublisherSerializers(queryset, many=True)
# return HttpResponse(json.dumps(ser.data), 'application/json')


# @api_view(['GET', 'POST'])
# def publisher_list(request):
#     if request.method == 'GET':
#         queryset = Publisher.objects.all()
#
#         s = serializers.PublisherSerializers(queryset, many=True)
#         return Response(s.data)
#
#     if request.method == 'POST':
#         s = serializers.PublisherSerializers(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.data, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def publisher_detail(request, pk):
#     try:
#         pub = Publisher.objects.get(pk=pk)
#     except Publisher.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'GET':
#         s = serializers.PublisherSerializers(pub)
#
#         return Response(s.data)
#
#     if request.method == 'PUT':
#         s = serializers.PublisherSerializers(pub, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data)
#         else:
#             return Response(status=status.HTTP_204_NO_CONTENT)
#
#     if request.method == 'DELETE':
#         pub.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class PublisherList(APIView):
#
#     def get(self, request):
#         queryset = Publisher.objects.all()
#         s = serializers.PublisherSerializers(queryset, many=True)
#         return Response(s.data)
#
#     def post(self, request):
#         s = serializers.PublisherSerializers(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

# class PublisherList(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = serializers.PublisherSerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class publishDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Publisher.objects.get(pk=pk)
#         except Publisher.DoesNotExist:
#             return Http404
#
#     def get(self, request, pk):
#         publisher = self.get_object(pk=pk)
#         s = serializers.PublisherSerializers(publisher)
#         return Response(s.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         publisher = self.get_object(pk=pk)
#         s = serializers.PublisherSerializers(publisher, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data)
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         publisher = self.get_object(pk=pk)
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class PublisherDetail(mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin,
#                       generics.GenericAPIView):
#
#     queryset = Publisher.objects.all()
#     serializer_class = serializers.PublisherSerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class PublisherList(generics.ListCreateAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = serializers.PublisherSerializers
#     permission_classes = (IsOwnerOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(operator=self.request.user)
#
#
# class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = serializers.PublisherSerializers
#     permission_classes = (IsOwnerOrReadOnly,)


# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = serializers.BookSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#
# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = serializers.BookSerializer
#     permission_classes = (permissions.IsAuthenticated)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # def perform_create(self, serializer):
    #
    #     serializer.save(operator=self.request.user)


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = serializers.PublisherSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)





@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'publishers': reverse('publisher_list', request=request, format=format),
            'books': reverse('book_list', request=request, format=format)
        }
    )
