#-*-coding:utf-8-*-
from datetime import datetime

from django.db import models
from users.models import UserProfile


class ItemInfo(models.Model):
    #UserId=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True,blank=True,verbose_name="所属用户ID")
    ItemId=models.IntegerField(primary_key=True,verbose_name="事项ID")
    Repeat=models.IntegerField(verbose_name="重复天数")
    DateCreated=models.DateTimeField(default=datetime.now,verbose_name="创建时间")
    IsDeleted=models.BooleanField(default=False,verbose_name="是否被删除")
    IsDone=models.BooleanField(default=False,verbose_name="已完成")
    class Meta:
        verbose_name = '待办事项'

    def __str__(self):
        return self.ItemId.__str__()

class ItemContent(models.Model):
    ItemId=models.ForeignKey(ItemInfo,null=True,on_delete=models.CASCADE,verbose_name="所属待办事项")
    ContentId = models.IntegerField(verbose_name="内容ID")
    Content=models.TextField(verbose_name="事项内容")
    Title=models.CharField(max_length=256,default="未填写",verbose_name="事项标题")
    DateCreated=models.DateTimeField(default=datetime.now,verbose_name="创建时间")
    TagId=models.IntegerField(verbose_name="事项类型")
    class Meta:
        verbose_name = 'todo item content'

    def __str__(self):
        return self.ContentId.__str__()