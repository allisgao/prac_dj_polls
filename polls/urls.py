#! python3
# Author: George Gao, gaojz017@163.com
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]
