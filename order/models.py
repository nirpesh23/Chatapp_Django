from django.db import models
from customer.models import Customer
from medicine.models import Medicine


# Create your models here.

class Order(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )

    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    Medicine=models.ForeignKey(Medicine,on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)



class ReturnMedicine(models.Model):
    name=models.CharField(max_length=40)
    medicine=models.CharField(max_length=50)
    Reason = models.TextField(help_text="Please confirm the return by stating the appropriate reason for the return")
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)    
    date= models.DateField(auto_now_add=True,null=True)
    date_ordersuccess = models.DateField()
    def __str__(self):
        return self.name
