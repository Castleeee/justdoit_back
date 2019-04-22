from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    #继承系统的users类
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #增加org
    org = models.CharField(
        'Organization', max_length=128, blank=True)
    #增加telphone
    telephone = models.CharField(
        'Telephone', max_length=50, blank=True)

    mod_date = models.DateTimeField('Last modified', auto_now=True)

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return self.user.__str__()