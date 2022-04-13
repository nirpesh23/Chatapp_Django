from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
# from MedicMandu import medicine
from medicine.models import Medicine
# Create your views here.

def home_view(request):
    medicines=Medicine.objects.all()
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        counter=medicine_ids.split('|')
        medicine_count_in_cart=len(set(counter))
    else:
        medicine_count_in_cart=0
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'medicmandu/index.html',{'medicines':medicines,'medicine_count_in_cart':medicine_count_in_cart})
################################################################




def search_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    medicines=Medicine.objects.all().filter(medname__icontains=query)
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        counter=medicine_ids.split('|')
        medicine_count_in_cart=len(set(counter))
    else:
        medicine_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"

    if request.user.is_authenticated:
        return render(request,'medicmandu/user_home.html',{'medicines':medicines,'word':word,'medicine_count_in_cart':medicine_count_in_cart})
    return render(request,'medicmandu/index.html',{'medicines':medicines,'word':word,'medicine_count_in_cart':medicine_count_in_cart})



##################################################

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()



def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('user-home')
    else:
        return redirect('admin-dashboard')



from django.shortcuts import render
from customer.views import is_customer
from django.contrib.auth.decorators import login_required,user_passes_test
from customer.models import Customer
from order.models import Order
from medicine.models import Medicine as med


@login_required(login_url='login')
def payment_success_view(request):
    # Here we will place order | after successful payment
    # we will fetch customer  mobile, address, Email
    # we will fetch product id from cookies then respective details from db
    # then we will create order objects and store in db
    # after that we will delete cookies because after order placed...cart should be empty
    customer=Customer.objects.get(user_id=request.user.id)
    medicines=None
    email=None
    mobile=None
    address=None
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        if medicine_ids != "":
            medicine_id_in_cart=medicine_ids.split('|')
            Medicine=med.objects.all().filter(id__in = medicine_id_in_cart)
            # Here we get products list that will be ordered by one customer at a time

    # these things can be change so accessing at the time of order...
    if 'email' in request.COOKIES:
        email=request.COOKIES['email']
    if 'mobile' in request.COOKIES:
        mobile=request.COOKIES['mobile']
    if 'address' in request.COOKIES:
        address=request.COOKIES['address']

    # here we are placing number of orders as much there is a products
    # suppose if we have 5 items in cart and we place order....so 5 rows will be created in orders table
    # there will be lot of redundant data in orders table...but its become more complicated if we normalize it
    for Medicine in Medicine:
        Order.objects.get_or_create(customer=customer,Medicine=Medicine,status='Pending',email=email,mobile=mobile,address=address)

    # after order placed cookies should be deleted
    response = render(request,'medicmandu/payment_success.html')
    response.delete_cookie('medicine_ids')
    response.delete_cookie('email')
    response.delete_cookie('mobile')
    response.delete_cookie('address')
    return response
