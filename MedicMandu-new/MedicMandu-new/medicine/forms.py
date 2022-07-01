from django import forms
from django.contrib.auth.models import User
from . import models



class MedicineForm(forms.ModelForm):
    class Meta:
        model=models.Medicine
        fields=['name','price','description','product_image']