from django import forms
from medicine.models import Medicine



class medicineForm(forms.ModelForm):
    class Meta:
        model=Medicine
        fields=['medname','medtype' , 'medmanufacturdate' , 'medexpirydate' , 'manufacturer'  , 'description' , 'medicine_image' , 'price'      ] 


