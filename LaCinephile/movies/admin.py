from django.contrib import admin
from .models import Now_Showing, Up_Comming
from django.db import models
from django.forms import Textarea
# Register your models here.

admin.site.register(Now_Showing)
admin.site.register(Up_Comming)



class RulesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 2,
                                  'cols': 40,
                                  'style': 'height: 1em;'})},
    }