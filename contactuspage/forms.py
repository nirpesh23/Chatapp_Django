from django import forms
from django.contrib.auth.models import User

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=80)
    Email = forms.EmailField()
    Phone = forms.CharField(max_length=10)
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
