from django.contrib.auth import login
from django.contrib.auth import views as auth_views
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

    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


]