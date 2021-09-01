from django.urls import path
from . import views

urlpatterns = [
    
    path('prices/', views.prices),
    path('book/', views.book),
    path('hall-json/',views.get_json_hall_data, name="hall-json"),
    path('test/', views.movie_detail),

]