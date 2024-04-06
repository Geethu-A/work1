from django import forms
from . models import *
class Teacher_form(forms.ModelForm):
    class Meta():
        model=Teacher
        fields="__all__"