from .models import Registration
from django import forms
class Registration2(forms.Form):
    name=forms.CharField()
    password=forms.CharField()
    email=forms.EmailField()
    cno=forms.CharField()
  
class Login(forms.Form):
    reg_id=forms.CharField()
    password=forms.CharField()