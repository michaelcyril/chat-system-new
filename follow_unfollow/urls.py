from django.urls import path
from .views import *
app_name = 'follow_unfollow'
urlpatterns = [
    path('following',follow),
    path('accepting',accept),
    path('unfollowing',unfollow),
]
