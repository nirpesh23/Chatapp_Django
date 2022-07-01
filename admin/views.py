from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
import customer
from customer.models import Customer, Prescription
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

from .forms import medicineForm
@login_required(login_url='adminlogin')
def adminaddmedicineview(request):
    MedicineForm=medicineForm()
    if request.method=='POST':
        MedicineForm=medicineForm(request.POST, request.FILES)
        if MedicineForm.is_valid():
            MedicineForm.save()
        return HttpResponseRedirect('adminmedicines')
    return render(request,'medicmandu/adminaddmedicine.html',{'MedicineForm':MedicineForm})



@login_required(login_url='adminlogin')
def updatemedicineview(request,pk):
    medicine=Medicine.objects.get(id=pk)
    MedicineForm=medicineForm(instance=medicine)
    if request.method=='POST':
        MedicineForm=medicineForm(request.POST,request.FILES,instance=medicine)
        if MedicineForm.is_valid():
            MedicineForm.save()
            return redirect('adminmedicines')
    return render(request,'medicmandu/adminupdatemed.html',{'MedicineForm':MedicineForm})



@login_required(login_url='adminlogin')
def deletemedicineview(request,pk):
    product=Medicine.objects.get(id=pk)
    product.delete()
    return redirect('adminmedicines')

from order.models import Order
from customer.models import Customer

@login_required(login_url='adminlogin')
def viewbooking(request):
    orders=Order.objects.all()
    orderedmeds=[]
    orderers=[]
    for order in orders:
        orderedmed=Medicine.objects.all().filter(id=order.Medicine.id)
        ordereder=Customer.objects.all().filter(id = order.customer.id)
        orderedmeds.append(orderedmed)
        orderers.append(ordereder)
    return render(request,'medicmandu/viewbook.html',{'data':zip(orderedmeds,orderers,orders)})
from order.forms import OrderForm
@login_required(login_url='adminlogin')
def deleteorderview(request,pk):
    order=Order.objects.get(id=pk)
    order.delete()
    return redirect('viewbooking')


@login_required(login_url='adminlogin')
def updatebookingview(request,pk):
    order=Order.objects.get(id=pk)
    orderForm=OrderForm(instance=order)
    if request.method=='POST':
        orderForm=OrderForm(request.POST,instance=order)
        if orderForm.is_valid():
            orderForm.save()
            return redirect('viewbooking')
    return render(request,'medicmandu/updateorder.html',{'orderForm':orderForm})

from order.models import ReturnMedicine
@login_required(login_url='adminlogin')
def viewReturnrequest(request):
    returnreq=ReturnMedicine.objects.all().order_by('-id')
    return render(request,'medicmandu/viewrequests.html',{'returnreq':returnreq})
from customer.models import Prescription
@login_required(login_url='adminlogin')
def Viewprescription(request):
    Prescriptions=Prescription.objects.all().order_by('-id')
    return render(request,'medicmandu/Viewprescription.html',{'Prescriptions':Prescriptions})