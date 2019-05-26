#-*-coding:utf-8-*-
from django.urls import path
#from .views import
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

app_name = 'users'
urlpatterns = [
    path(r'login/', obtain_jwt_token),  # jwt的token验证
    path(r'tokenRefresh/', refresh_jwt_token),  # token刷新   
    #path(r"")
]
# path(r'register/', views.register, name='register'),#注册
# path(r'login/', views.login, name='login'),#登录
# path(r'user/<int:id>/profile/', views.profile, name='profile'),#查看个人信息
# path(r'user/<int:id>/profile/update/', views.profile_update, name='profile_update'),#个人信息更新
# path(r'user/<int:id>/pwdchange/', views.pwd_change, name='pwd_change'),#改密码
# path(r'logout/', views.logout, name='logout'),#登出