from django.contrib.auth import login
from django.urls import path
from . import views
from movies.views import user_movies

urlpatterns = [
    path('register/',views.register),
    path('login/', views.user_login),
    path('logout/', views.logout_user),
    path('dashboard/', user_movies),
    path('profile/', views.user_profile),
    path('update_profile/', views.update_profile),
    path('password/', views.change_password),

]