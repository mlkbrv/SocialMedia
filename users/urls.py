from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
       path('login/', user_login, name='login'),
       path('logout/', user_logout, name='logout'),
       path('',index,name='index'),
]
