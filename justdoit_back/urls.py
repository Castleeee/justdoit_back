"""justdoit_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import xadmin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path(r'accounts/', include('users.urls')),#用户的API
    path(r'items/', include('todolist.urls')),#todo的API
    path(r'docs/', include_docs_urls(title='API文档')),#REST的文档生成
    path(r'api-auth/', include('rest_framework.urls')),#rest的权限验证
    path(r'api-token-auth/', views.obtain_auth_token),#api的token验证
    path(r'jwt-token-auth/', obtain_jwt_token),#jwt的token验证
    path(r'jwt-token-refresh/', refresh_jwt_token)#token刷新
]
