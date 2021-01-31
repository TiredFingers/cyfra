from django import forms
from .models import Car


class CarForm(forms.Form):
    car = forms.CharField(widget=forms.HiddenInput, required=True)
    coords = forms.CharField(widget=forms.TextInput, required=True)

    def clean(self):

        cleaned_data = super().clean()

        coords = cleaned_data.get('coords', None)

        if coords:

            parsed = coords.split(" ")

            if len(parsed) < 2 or not parsed[0].isnumeric() or not parsed[1].isnumeric():
                raise forms.ValidationError("Неправильный формат координат")
