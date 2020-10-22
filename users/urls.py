"""为应用程序users定义URL模式"""
from django.conf.urls import url
# from django.contrib.auth.views import login
from django.contrib.auth.views import LoginView
from . import views

urlpatterns=[
    # 原文
    #登录页面
    # url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),

    # 改
    #登录界面  LoginView.as_view后面要加上()
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),

    url(r'^logout/$',views.logout_view,name='logout'),

    url(r'^register/$',views.register,name='register'),
]

# from django.urls import re_path
# from django.contrib.auth.views import LoginView
# from . import views
# """为应用程序users定义的url模式"""
# app_name = 'users'
# urlpatterns = [
#
# #登录页面
# re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'),
# name='login'),
# ]