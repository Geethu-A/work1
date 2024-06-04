from django import forms
from app.models import *
class Productform(forms.ModelForm):
    class Meta:
        model=Appointmentsss
        fields='__all__'