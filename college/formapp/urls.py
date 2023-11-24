from . import views
from django.urls import path

app_name='formapp'

urlpatterns = [
    path('add/',views.create_view,name='register'),
    path('ajax/load-courses/',views.load_courses,name='ajax_load_courses'),
]