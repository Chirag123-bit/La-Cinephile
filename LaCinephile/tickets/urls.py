from django.urls import path
from . import views
from movies.views import user_movies

urlpatterns = [
    path('detail/<int:uid>/<int:mid>', views.detail),

]