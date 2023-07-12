from django.urls import path
from .views import *
app_name = 'authentication'
urlpatterns = [
    path('login',login_user),
    path('logout',logout_user),
    path('register',Register_Users),
    path('all-user',AllUser),
]
