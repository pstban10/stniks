from django import forms
from django.forms import ModelForm
from .models import TestClass


class TestClassForm(ModelForm):
    class Meta:
        model = TestClass
        fields = [
            "full_name",
            "date",
            "phone",
            "hour"
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
