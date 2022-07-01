from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from . import models

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']


class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model=models.Prescription
        fields=['user_prescription', 'mobile']

    