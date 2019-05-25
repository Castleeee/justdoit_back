#-*-coding:utf-8-*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    name=models.CharField(max_length=30,null=True,blank=True,verbose_name="姓名")
    birthday=models.DateField(null=True,blank=True,verbose_name="生日")
    gender=models.CharField(max_length=10,choices=(("male","男"),("female","女")),default="male")
    mobile=models.CharField(max_length=11,default="",verbose_name="手机号码")
    email = models.EmailField(max_length=100,null=True,blank=True,verbose_name="邮箱")
    class Meta:
        verbose_name = '用户'

    def __str__(self):
        return self.name.__str__()

class VerifyCode(models.Model):
    code=models.CharField(max_length=10,verbose_name="验证码")
    mobile=models.CharField(max_length=11,verbose_name="手机号码")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    class Meta:
        verbose_name = '短信验证'

    def __str__(self):
        return self.mobile.__str__()