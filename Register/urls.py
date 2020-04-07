from django.contrib import admin
from django.urls import path, include

from Register import views

urlpatterns = [
    path('', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout_user, name='logout'),
]