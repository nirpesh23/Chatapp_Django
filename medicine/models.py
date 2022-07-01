from email.policy import default
from django.db import models



Medicinetype_CHOICES = [
    ('l', 'Liquid'),
    ('tab', 'Tablet'),
    ('cap', 'Capsules'),
    ('drops', 'Drops'),
    ('ins','Insulin'),
    ('Topical','Topical medicines'),
    ('Imp','Implants')
]
class manufacturer(models.Model):
    companyname = models.CharField(max_length=55)
    companycountry = models.CharField(max_length=55)
    companyestd = models.CharField(max_length=55)
    companycontact = models.CharField(max_length=55)
    companycertified = models.BooleanField()
    
    def __str__(self):
        return self.companyname 
# Create your models here.
class Medicine(models.Model):
    medname=models.CharField(max_length=55)
    medtype = models.CharField(max_length=10,choices=Medicinetype_CHOICES,default='Liquid',null=True)
    # medmanufacturere =models.ForeignKey(manufacturer,on_delete=models.CASCADE)
    medmanufacturdate = models.DateField(blank=False , null=True)
    medexpirydate = models.DateField(blank= False, null=True )
    manufacturer = models.CharField(max_length=150 , blank=False ,null=True)
    description=models.CharField(max_length=40,null=True)
    medicine_image= models.ImageField(upload_to='medicine/',default='default.jpg')
    slug= models.SlugField(max_length=150,null=True)
    price = models.PositiveIntegerField(null=True)
    in_stock = models.BooleanField(default= True,null=True)
    # is_active = models.BooleanField(default=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.medname

