from rest_framework import serializers

from . import models


# 序列化
# class PublisherSerializers(serializers.Serializer):
# id = serializers.IntegerField(read_only=True)
# name = serializers.CharField(max_length=32)
# address = serializers.CharField(max_length=128)
#
# def create(self, validated_data):
#     return models.Publisher.objects.create(**validated_data)
#
# def update(self, instance, validated_data):
#     instance.name = validated_data.get('name', instance.name)
#     instance.address = validated_data.get('address', instance.address)
#     return instance


# 序列化
class PublisherSerializers(serializers.ModelSerializer):
    operator = serializers.ReadOnlyField(source='operator.username')

    # book_set = BookSerializers(many=True, read_only=True)
    class Meta:
        model = models.Publisher
        fields = (
            'id',
            'name',
            'address',
            'operator',
        )


class BookSerializers(serializers.HyperlinkedModelSerializer):
    publisher_name = serializers.StringRelatedField(source='publisher.name')

    # publisher_name = PublisherSerializers()
    class Meta:
        model = models.Book
        fields = (
            'id',
            'name',
            'publisher_name',
            'publisher'
        )
