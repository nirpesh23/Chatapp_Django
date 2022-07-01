from django.urls import path, include
from customer.models import Customer , Prescription 
from medicine.models import Medicine , manufacturer
from order.models import Order , ReturnMedicine
from pharmacy.models import payment

from rest_framework import routers, serializers, viewsets


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['user','profile_pic','address','mobile']
class PrescitptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prescription
        fields = ['user_prescription' , 'mobile']

class MeedicineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medicine
        fields = ['medname','medtype','medmanufacturdate','medexpirydate','manufacturer','description','medicine_image','slug','price']

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = manufacturer
        fields = ['companyname','companycountry','companyestd','companycontact','companycertified']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['customer','Medicine','email','address','mobile','order_date','status']

class returnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReturnMedicine
        fields = ['name','meddicine','Reason','email','address','mobile','date','date_ordersuccess']

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = payment
        fields = ['Order','paymentamount','paymentdate','paymenttype','paymentreceiver']



