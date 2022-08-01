from django import forms

from ..models.flight import Flight

class HiddenInput(forms.DateInput):
    input_type = 'hidden'

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['id']
        widgets = {
            'id': HiddenInput()
        }
