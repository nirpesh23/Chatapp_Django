from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from . import forms , models
from django.contrib.auth.decorators import login_required,user_passes_test
from medicine.models import Medicine
from django.contrib.auth.models import Group
def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()



# Create your views here.
@login_required(login_url='login')
@user_passes_test(is_customer)
def user_home_view(request):
    medicines=Medicine.objects.all()
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        counter=medicine_ids.split('|')
        medicine_count_in_cart=len(set(counter))
    else:
        medicine_count_in_cart=0
    return render(request,'medicmandu/customer_base.html',{'medicines':medicines,'medicine_count_in_cart':medicine_count_in_cart})


# shipment address before placing order
@login_required(login_url='login')
def useraddressview(request):
    # this is for checking whether product is present in cart or not
    # if there is no product in cart we will not show address form
    medicine_in_cart=False
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        if medicine_ids != "":
            medicine_in_cart=True
    #for counter in cart
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        counter=medicine_ids.split('|')
        medicine_count_in_cart=len(set(counter))
    else:
        medicine_count_in_cart=0

    addressForm = forms.AddressForm()
    if request.method == 'POST':
        addressForm = forms.AddressForm(request.POST)
        if addressForm.is_valid():
            # here we are taking address, email, mobile at time of order placement
            # we are not taking it from customer account table because
            # these thing can be changes
            email = addressForm.cleaned_data['Email']
            mobile=addressForm.cleaned_data['Mobile']
            address = addressForm.cleaned_data['Address']
            #for showing total price on payment page.....accessing id from cookies then fetching  price of product from db
            total=0
            if 'medicine_ids' in request.COOKIES:
                medicine_ids = request.COOKIES['medicine_ids']
                if medicine_ids != "":
                    medicine_id_in_cart=medicine_ids.split('|')
                    medicines=Medicine.objects.all().filter(id__in = medicine_id_in_cart)
                    for p in medicines:
                        total=total+p.price

            response = render(request, 'medicmandu/payment.html',{'total':total})
            response.set_cookie('email',email)
            response.set_cookie('mobile',mobile)
            response.set_cookie('address',address)
            return response
    return render(request,'medicmandu/useraddress.html',{'addressForm':addressForm,'medicine_in_cart':medicine_in_cart,'medicine_count_in_cart':medicine_count_in_cart})


@login_required(login_url='login')
@user_passes_test(is_customer)
def profileview(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    return render(request,'medicmandu/profile.html',{'customer':customer})


@login_required(login_url='login')
def useraddressview2(request):
    # this is for checking whether product is present in cart or not
    # if there is no product in cart we will not show address form
    medicine_in_cart=False
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        if medicine_ids != "":
            medicine_in_cart=True
    #for counter in cart
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        counter=medicine_ids.split('|')
        medicine_count_in_cart=len(set(counter))
    else:
        medicine_count_in_cart=0

    
    if request.method == 'POST':
        total=0
        if 'medicine_ids' in request.COOKIES:
            medicine_ids = request.COOKIES['medicine_ids']
            if medicine_ids != "":
                medicine_id_in_cart=medicine_ids.split('|')
                medicines=Medicine.objects.all().filter(id__in = medicine_id_in_cart)
                for p in medicines:
                    total=total+p.price
    return render(request,'medicmandu/useraddress2.html',{'medicine_in_cart':medicine_in_cart,'medicine_count_in_cart':medicine_count_in_cart})




def user_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('userlogin')
    return render(request,'medicmandu/signup.html',context=mydict)


