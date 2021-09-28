from django.db import models
from django.db.models import fields
from django.forms import ModelForm, Textarea
from .models import Movie, Now_Showing, Up_Comming

#Movie's Form
class NowShowingForm(ModelForm):
    class Meta:
        model = Now_Showing
        fields = "__all__"

class UpCommingForm(ModelForm):
    class Meta:
        model = Up_Comming
        fields = "__all__"