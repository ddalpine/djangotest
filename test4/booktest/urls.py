#coding:utf8
"""test4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^(\d+)/(\d+)$', views.show,name='show'),
    url(r'^index2$', views.index2,name='index2'),
    url(r'^user1',views.user1,name='user1'),
    url(r'^user2',views.user2,name='user2'),
    url(r'^htmlTest$',views.htmlTest,name='htmlTest'),
    url(r'^csrf1$',views.csrf1),
    url(r'^csrf2$',views.csrf2),
    url(r'^verifyCode$',views.verifyCode),
    url(r'^verifyTest1$',views.verifyTest1),
    url(r'^verifyTest2$',views.verifyTest2),

]
