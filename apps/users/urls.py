#-*-coding:utf-8-*-
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path(r'register/', views.register, name='register'),#注册
    path(r'login/', views.login, name='login'),#登录
    path(r'user/<int:id>/profile/', views.profile, name='profile'),#查看个人信息
    path(r'user/<int:id>/profile/update/', views.profile_update, name='profile_update'),#个人信息更新
    path(r'user/<int:id>/pwdchange/', views.pwd_change, name='pwd_change'),#改密码
    path(r'logout/', views.logout, name='logout'),#登出
]
