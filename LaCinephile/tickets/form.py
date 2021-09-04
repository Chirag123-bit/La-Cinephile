from django import forms 
from halls.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"