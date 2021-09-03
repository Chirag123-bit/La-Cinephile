from django.urls import path
from . import views

urlpatterns = [
    
    path('prices/', views.prices),
    path('book/', views.book),
    path('test/', views.movie_json, name="test"),
    path('test-hall/<int:movie>', views.hall_json, name="test-hall"),
    path('day/<int:mid>/<int:hid>', views.date_json, name="day"),
    path('time/<int:mid>/<int:hid>/<str:date>', views.time_json, name="time"),
    path('price/<int:hmid>', views.dis_price_json, name="price"),

]