#-*-coding:utf-8-*-
#SettingCode here
__author__ = "a_little_rubbish"
__date__ = "2019-05-25 11:15"
from rest_framework import serializers

class ItemInfoSerializer(serializers.Serializer):
    Repeat=serializers.IntegerField(max_value=365,required=True)
    DateCreated=serializers.DateTimeField(required=True)
    IsDeleted=serializers.BooleanField(default=False)
    IsDone=serializers.BooleanField(default=False)