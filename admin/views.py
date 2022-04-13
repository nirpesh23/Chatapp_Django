from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from customer.models import Customer
from medicine.models import Medicine
from order.models import Order
# Create your views here.
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    # for cards on dashboard
    customercount=Customer.objects.all().count()
    medicinecount=Medicine.objects.all().count()
    ordercount=Order.objects.all().count()

    # for recent order tables
    orders=Order.objects.all()
    ordered_medicines=[]
    ordered_bys=[]
    for order in orders:
        ordered_medicine=Medicine.objects.all().filter(id=order.Medicine.id)
        ordered_by=Customer.objects.all().filter(id = order.customer.id)
        ordered_medicines.append(ordered_medicine)
        ordered_bys.append(ordered_by)

    mydict={
    'customercount':customercount,
    'medicinecount':medicinecount,
    'ordercount':ordercount,
    'data':zip(ordered_medicines,ordered_bys,orders),
    }
    return render(request,'medicmandu/admin_dashboard.html',context=mydict)

@login_required(login_url='adminlogin')
def viewcustomer(request):
    customers=Customer.objects.all()
    return render(request,'medicmandu/viewcustomer.html',{'customers':customers})

from customer.forms import CustomerUserForm , CustomerForm
from . import models

@login_required(login_url='adminlogin')
def updatecustomer(request,pk):
    customer=Customer.objects.get(id=pk)
    user=models.User.objects.get(id=customer.user_id)
    userForm=CustomerUserForm(instance=user)
    customerForm=CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=CustomerUserForm(request.POST,instance=user)
        customerForm=CustomerForm(request.POST,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return redirect('view-customer')
    return render(request,'medicmandu/adminupdatecustomer.html',context=mydict)

@login_required(login_url='adminlogin')
def adminmedicineview(request):
    medicines=Medicine.objects.all()
    return render(request,'medicmandu/adminmedicines.html',{'medicine':medicines})
@login_required(login_url='adminlogin')
def deletecustomer(request,pk):
    customer=Customer.objects.get(id=pk)
    user=models.User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return redirect('view-customer')