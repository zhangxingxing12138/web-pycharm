from rest_framework import serializers
from . import models


# class PubliserSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=12)
#     address = serializers.CharField(max_length=128)
#
#     def create(self, validated_data):
#         return models.Publisher.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.address = validated_data.get('address', instance.address)
#         return instance


class PublisherSerializers(serializers.ModelSerializer):
    operator = serializers.ReadOnlyField(source='operator.username')

    # operator = serializers.CharField(source='get_User_display')
    class Meta:
        model = models.Publisher
        fields = (
            'id',
            'name',
            'address',
            'operator'

        )

        extra_kwargs = {'address': {'required': False}}

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.address = validated_data.get('address', instance.address)
    #     return instance


class BookSerializer(serializers.HyperlinkedModelSerializer):
    publisher = serializers.StringRelatedField(source='publisher.name')

    # publisher = PublisherSerializers(read_only=True)

    class Meta:
        model = models.Book
        fields = (
            'id',
            'title',
            'publisher'
        )
