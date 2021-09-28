from django.urls import path
from . import views
from movies.views import user_movies

#Ticket's URL
urlpatterns = [
    path('detail/<int:uid>/<int:mid>', views.detail),
    path('cancle_tickets/<int:uid>/<int:mid>', views.cancle_tickets)

]