from django.urls import path
from . import views

urlpatterns = [
    
    path('dashboard/', views.dashboard),
    path('show_user/', views.show_user),
    path('show_movies/', views.show_movie),
    path('update_movie/<int:movie_id>', views.update_movie),
    path('delete_movie/<int:movie_id>', views.delete_movie),
    path('promote/<int:user_id>', views.promote_user),
    path('remove/<int:user_id>', views.delete_user),
    path('update/<int:user_id>', views.update_user),
    path('deactivate/<int:user_id>', views.deactivate),
    path('activate/<int:user_id>', views.activate),

    path('up_movies/', views.up_movie),
    path('update_upmovie/<int:movie_id>', views.update_movie),
    path('delete_upmovie/<int:movie_id>', views.delete_movie),

    path('show_hall/', views.show_hall),
    path('update_hall/<int:hall_id>', views.update_hall),
    path('delete_hall/<int:hall_id>', views.delete_hall),

    path('hall_category/', views.hall_category),
    path('update_hallCategory/<int:hallCat_id>', views.update_hall_cat),
    path('delete_hallCategory/<int:hallCat_id>', views.delete_hall_cat),

]