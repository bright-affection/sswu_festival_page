from django.urls import path
from .views import boothinfo, boothsearch

app_name = 'booth'

urlpatterns = [
    path('', boothinfo, name='boothinfo'),
    path('search/', boothsearch, name='boothsearch'),
]