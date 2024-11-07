from django import forms
from .models import PrData


class PrDataForm(forms.ModelForm):

    class Meta:
        model = PrData
        fields = '__all__'
