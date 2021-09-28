
from .models import Hall, Category, Movie_Hall
from django.forms import ModelForm


#Hall's Form
class HallForm(ModelForm):
    class Meta:
        model = Hall
        fields = "__all__"

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class MovieHallForm(ModelForm):
    class Meta:
        model = Movie_Hall
        fields = "__all__"