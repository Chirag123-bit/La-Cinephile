from tickets.models import Categories
from django import forms 
from halls.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"