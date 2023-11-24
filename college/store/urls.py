from . import views
from django.urls import path

app_name='store'
urlpatterns = [
    path('',views.allprod,name='allprod'),
    path('register/',views.register_user,name='register_user'),
    path('login/', views.login_user, name='login_user'),
    # path('form/',views.newform,name='form'),
    #path('form/',views.user_registration,name='form'),
    path('logout/',views.logout,name='logout'),
    path('submit/',views.submit_form,name='submit'),
]
