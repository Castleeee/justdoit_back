#-*-coding:utf-8-*-
from django.db import models
from users.models import UserProfile
class ItemInfo(models.Model):
    UserId=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    ItemId=models.IntegerField()
    Repeat=models.IntegerField()
    DateCreated=models.DateTimeField()
    IsDeleted=models.BooleanField()
    IsDone=models.BooleanField()
    class Meta:
        verbose_name = 'todo item'

    def __str__(self):
        return self.ItemId.__str__()

class ItemContent(models.Model):
    ItemId=models.ForeignKey(ItemInfo,on_delete=models.CASCADE)
    ContentId = models.IntegerField()
    Content=models.CharField()
    Title=models.CharField()
    DateCreated=models.DateTimeField()
    TagId=models.IntegerField()
    class Meta:
        verbose_name = 'todo item content'

    def __str__(self):
        return self.ContentId.__str__()