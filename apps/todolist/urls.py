#-*-coding:utf-8-*-
from django.urls import path
from . import views

app_name = 'iteminfo'
urlpatterns = [


]

# path(r'iteminfo/<int:itemid>/', views.getiteminfo, name='iteminfo'),  # 获得item所有内容
# path(r'itemid/<int:itemid>/', views.getitem, name='itemid'),  # 获得该item
# path(r'repeat/<int:itemid>/', views.isrepeat, name='isrepeat'),  # 剩余重复日期
# path(r'createtime/<int:itemid>/', views.getdatecreated, name='getdatecreated'),  # item创建时间
# path(r'isdeleted/<int:itemid>/', views.isdeleted, name='isdeleted'),  # 是否已被删除
# path(r'isdone/<int:id>/', views.isdone, name='isdone'),  # 已完成
#
# path(r'content/<int:itemid>/', views.getcontent, name='content'),  # 获得contnet所有内容
# path(r'contentid/<int:itemid>/', views.getcontentid, name='getcontentid'),  # 获得内容id
# path(r'contenttitle/<int:contentid>/', views.getcontenttitle, name='getcontentitle'),  # 获得标题
# path(r'content/<int:contentid>/', views.getcontent, name='getcontent'),  # 获得内容
# path(r'contentcreatetime/<int:contentid>/', views.getcontentcreatetime, name='getcontentcreatetime'),  # 获得内容创建时间
# path(r'contenttagid/<int:contentid>/', views.getcontenttagid, name='getcontenttagid'),  # 获得标签id
#
# path(r'onesitem/<int:userid>/<int:datestart>/<int:dateend>', views.getonesitem, name='getonesitem'),  # 获得用户的todo
