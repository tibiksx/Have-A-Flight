from django import forms

from ..models.ticket import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['seat']
