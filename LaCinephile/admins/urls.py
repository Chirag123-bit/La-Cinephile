from django.urls import path
from . import views

urlpatterns = [
    
    path('dashboard/', views.dashboard, name="admin_dashboard"),
    path('show_user/', views.show_user),
    path('show_admin/', views.show_admin),

    path('show_movies/', views.show_movie),
    path('update_movie/<int:movie_id>', views.update_movie),
    path('delete_movie/<int:movie_id>', views.delete_movie),
    path('promote/<int:user_id>', views.promote_user),
    path('demote/<int:user_id>', views.demote_user),
    path('remove/<int:user_id>', views.delete_user),
    path('remove_admin/<int:user_id>', views.delete_admin),
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
    path('delete_hall_cat/<int:hallCat_id>', views.delete_hall_cat),

    path('movie_hall/', views.movie_hall),
    path('update_movie_hall/<int:mh_id>', views.update_movie_hall),
    path('delete_movie_hall/<int:hallCat_id>', views.delete_movie_hall),

    path('show_ticket/', views.show_ticket),
    path('purchase/<int:tic_id>', views.purchase),
    path('reserve/<int:tic_id>', views.reserve),
    path('cancle/<int:tic_id>', views.cancle),
    
    path('ticket_cat/', views.ticket_cat),
    path('update_tcat/<int:tc_id>', views.update_ticket_cat),
    path('delete_tcat/<int:tc_id>', views.delete_ticket_cat),
    
    path('show_payments/', views.payments),
    
    path('create_user/', views.create_User),
    path('create_ticket/', views.create_Ticket),
    path('create_category/', views.create_Category),

    path('add_hall/', views.add_hall),
    path('add_hall_cat/', views.add_hallCat),
    path('add_now_showing/', views.add_nowShowing),
    path('add_up_comming/', views.add_upComming),

    path('profile/', views.admin_profile, name="show_admin_profile"),
    path('update_profile/', views.update_profile),
    path('password/', views.change_password),


]