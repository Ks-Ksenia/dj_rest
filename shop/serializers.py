from rest_framework import serializers

from .models import Test

'''
Сериализаторы нужны для того, чтобы преобразовывать типы данные из формата json в типы данных питон,
и наоборот, из типов данных питов, в типы данных json формата

например, берём queryset, далее представляем это ввиде json, для отправки на клиентскую сторону, 
для этого используем сериализаторы

'''

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = '__all__'

#
# class TestSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=150)
#     tel = serializers.CharField(required=False, allow_blank=True, max_length=150)
#
#
#     def create(self, validated_data):
#         return Test.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.tel = validated_data.get('tel', instance.tel)
#         instance.save()
#         return instance