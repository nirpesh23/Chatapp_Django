from django import forms
from django.contrib.auth.models import User
from . import models


class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']
