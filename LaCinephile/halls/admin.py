from django.contrib import admin
from . models import Category, Hall, Movie_Hall
# Register your models here.

admin.site.register(Category)
admin.site.register(Hall)


class Movie_HallAdmin(admin.ModelAdmin):
    def get_hall(self, obj):
        return obj.hall.h_Name
    def get_movie(self, obj):
        return obj.movie.name
    
    get_hall.short_description = 'Hall Name'
    get_movie.short_description = 'Movie Name'
    list_display = [ 'get_hall', 'get_movie', 'time', 'day']


admin.site.register(Movie_Hall, Movie_HallAdmin)