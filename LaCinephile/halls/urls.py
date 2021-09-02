from django.urls import path
from . import views

urlpatterns = [
    
    path('prices/', views.prices),
    path('book/', views.book),
    path('test/', views.movie_json, name="test"),
    path('test-hall/<int:movie>', views.hall_json, name="test-hall"),
    path('day/<int:id>', views.day_json, name="day"),

]