from django import forms
from .models import PrData, Persona


class PrDataForm(forms.ModelForm):

    class Meta:
        model = PrData
        fields = '__all__'


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = '__all__'
