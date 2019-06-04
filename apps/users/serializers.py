#-*-coding:utf-8-*-
#SettingCode here
__author__ = "a_little_rubbish"
__date__ = "2019-06-04 19:52"

#import your model here
import re
from datetime import datetime, timedelta
MAIL_MOBILE='/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/'
from users.models import VerifyCode
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class mailSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=100)

    # 函数名必须：validate + 验证字段名
    def validate_mobile(self, mail):
        """
        手机号码验证
        """
        # 是否已经注册
        if User.objects.filter(mobile=mail).count():
            raise serializers.ValidationError("邮箱已经注册")

        # 是否合法
        if not re.match(MAIL_MOBILE, mail):
            raise serializers.ValidationError("邮箱非法")

        # 验证码发送频率
        # 60s内只能发送一次
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mail=mail).count():
            raise serializers.ValidationError("发送频率过快")

        return mail
#your class&function here
