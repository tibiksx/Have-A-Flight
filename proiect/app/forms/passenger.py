from django import forms

from ..models.passenger import Passenger

class DateInput(forms.DateInput):
    input_type = 'date'

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['name', 'date_of_birth', 'tel_no']
        widgets = {
            'date_of_birth': DateInput()
        }
