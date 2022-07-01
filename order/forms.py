from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['status']


class ReturnForm(forms.ModelForm):
    class Meta:
        model=models.ReturnMedicine
        fields=['name','medicine' , 'Reason' , 'mobile' , 'email' , 'address','date_ordersuccess']



        
