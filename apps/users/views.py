#-*-coding:utf-8-*-

from .models import UserProfile
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets,status
from rest_framework.response import Response

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from random import choice
from .models import VerifyCode
from .serializers import mailSerializer
from apps.utils.sendMail import SendMail

User = get_user_model()

class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            #用户名和手机都能登录
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class mailCodeViewset(CreateModelMixin,viewsets.GenericViewSet):
    '''
    手机验证码
    '''
    serializer_class = mailSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        #验证合法
        serializer.is_valid(raise_exception=True)

        mail = serializer.validated_data["mail"]


        #生成验证码
        code = self.generate_code()

        sendmail = SendMail(code=code, mail=mail)

        if mail_status["code"] != 0:
            return Response({
                "mobile": mail_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mail=mail)
            code_record.save()
            return Response({
                "mail": mail
            }, status=status.HTTP_201_CREATED)
