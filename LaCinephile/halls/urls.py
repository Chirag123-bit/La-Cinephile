from django.urls import path
from . import views

urlpatterns = [
    
    path('prices/', views.prices),

]