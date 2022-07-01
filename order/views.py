from django.shortcuts import render
from customer.views import is_customer
from django.contrib.auth.decorators import login_required,user_passes_test
from customer.models import Customer
from order.forms import ReturnForm
from .models import Order
from medicine.models import Medicine 
# Create your views here.



@login_required(login_url='userlogin')
@user_passes_test(is_customer)
def order_view(request):
    customers=Customer.objects.get(user_id=request.user.id)
    orders=Order.objects.all().filter(customer_id = customers)
    ordered_Medicines=[]
    for order in orders:
        ordered_Medicine=Medicine.objects.all().filter(id=order.Medicine.id)
        ordered_Medicines.append(ordered_Medicine)

    return render(request,'medicmandu/order.html',{'data':zip(ordered_Medicines,orders)})




def send_returnrequest(request):
    ReturnForms=ReturnForm()
    if request.method == 'POST':
        ReturnForms = ReturnForm(request.POST)
        if ReturnForms.is_valid():
            ReturnForms.save()
            return render(request, 'medicmandu/sent_returnrequest.html')
    return render(request, 'medicmandu/send_returnrequest.html', {'ReturnForms':ReturnForms})


def ReturnPolicy(request):
    return render(request, 'medicmandu/returnpolicy.html')
