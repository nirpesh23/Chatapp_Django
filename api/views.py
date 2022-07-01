from .serializers import CustomerSerializer, ManufacturerSerializer, MeedicineSerializer, OrderSerializer, PaymentSerializer, PrescitptionSerializer, returnSerializer 


from rest_framework import  viewsets
from customer.models import Customer , Prescription 
from medicine.models import Medicine , manufacturer
from order.models import Order , ReturnMedicine
from pharmacy.models import payment

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescitptionSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MeedicineSerializer

class manufacturerViewSet(viewsets.ModelViewSet):
    queryset = manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReturnMedicineViewSet(viewsets.ModelViewSet):
    queryset = ReturnMedicine.objects.all()
    serializer_class = returnSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = payment.objects.all()
    serializer_class = PaymentSerializer

   