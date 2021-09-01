from django.contrib.auth import login
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register),
    path('login/', views.user_login),
    path('logout', views.logout_user),

]