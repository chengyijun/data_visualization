"""sfdv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path

from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('calc', views.calc, name='calc'),
    path('', views.index, name='index'),
    path('test1', views.test1, name='test1'),
    re_path(r'^test2/(\w+)/(\d+)$', views.test2, name='test2'),
    re_path(r'^test3/(?P<a>\w+)/(?P<b>\d+)$', views.test3, name='test3'),
    path('test4/<a>/<int:b>', views.test4, name='test4'),
    path('test5', views.test5, {'a': 'eef', 'b': 123}, name='test5'),
    path('showtest', views.showtest, name='showtest'),
    path('revtest', views.revtest, name='revtest')
]
