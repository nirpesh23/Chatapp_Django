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

# Create your models here.
class Medicine(models.Model):
    medname=models.CharField(max_length=55)
    medtype = models.CharField(max_length=10,choices=Medicinetype_CHOICES,default='Liquid',null=True)
    medmanufacturdate = models.DateField(blank=False , null=True)
    medexpirydate = models.DateField(blank= False, null=True )
    manufacturer = models.CharField(max_length=150 , blank=False ,null=True)
    description=models.CharField(max_length=40,null=True)
    medicine_image= models.ImageField(upload_to='medicine/',blank=True,null=True)
    slug= models.SlugField(max_length=150,null=True)
    price = models.PositiveIntegerField(null=True)
    in_stock = models.BooleanField(default= True,null=True)
    # is_active = models.BooleanField(default=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.medname
