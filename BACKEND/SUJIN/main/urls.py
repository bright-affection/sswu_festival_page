from django.urls import path
from .views import timetable

app_name = 'main'

urlpatterns = [
    path('timetable/', timetable, name='timetable'),
    # path('map/', map, name='map'),
]