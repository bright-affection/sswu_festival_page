from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainpage'

urlpatterns = [
    path('mainpage/', views.mainpage, name='mainpage'),
    path('administrator/', views.administrator, name='administrator'),
    path('info/', views.info_list, name='info'),
    path('info_write/', views.info_write, name='info_write'),
    path('info_post/<int:info_id>/', views.info_post, name='info_post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)