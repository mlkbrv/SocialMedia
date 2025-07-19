from django.urls import path

import posts
from .views import *
urlpatterns = [
    path('create/',create_post,name='create_post'),
    path('feed/',feed,name='feed'),
    path('like/',like_post,name='like'),
]
