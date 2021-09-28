from django.urls import path
from . import views

#Hall's URL
urlpatterns = [
    path('prices/', views.prices, name="show_prices"),
    path('book/', views.book, name="book_tickets"),
    path('test/', views.movie_json, name="test"),
    path('test-hall/<int:movie>', views.hall_json, name="test-hall"),
    path('day/<int:mid>/<int:hid>', views.date_json, name="day"),
    path('time/<int:mid>/<int:hid>/<str:date>', views.time_json, name="time"),
    path('price/<int:hmid>', views.dis_price_json, name="price"),
    path('seats/<int:id>', views.seats_json, name="Reserved"),

    path('khalti-request/', views.KhaltiRequestView.as_view(), name="khaltirequest"),
    path('khalti-verify/', views.KhaltiVerifyView.as_view(), name="khaltiverify"),

]