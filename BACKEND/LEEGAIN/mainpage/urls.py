from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'mainpage'

urlpatterns = [
    path('mainpage/', views.mainpage, name='mainpage'),
    path('administrator/', views.administrator, name='administrator'),
    path('info/', views.info_list, name='info'),
    path('info_write/', views.info_write, name='info_write'),
    path('info_post/<int:info_id>/', views.info_post, name='info_post'),
]
