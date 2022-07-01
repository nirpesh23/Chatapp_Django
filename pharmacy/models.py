from django.db import models
from order.models import Order

choices = [
    'esewa','esewa',
    'khalti','khalti',
    'cash','cash'
]

# Create your models here.
class payment(models.Model):
    Order = models.ForeignKey(Order,on_delete=models.CASCADE)
    paymentamount=models.IntegerField()
    paymentdate=models.DateField()
    paymenttype=models.CharField(choices, default='cash' , max_length=10)
    paymentreceiver = models.CharField(max_length=10)

