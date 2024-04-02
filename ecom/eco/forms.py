from django import forms
from eco.models import *
class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'