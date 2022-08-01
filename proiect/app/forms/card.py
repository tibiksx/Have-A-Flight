from django import forms

from ..models import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'card_no', 'exp_month', 'exp_year']
