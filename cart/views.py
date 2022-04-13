from django.shortcuts import render
from medicine.models import Medicine
from django.contrib import messages
# Create your views here.
def addtocartview(request,pk):
    medicines=Medicine.objects.all()

    #for cart counter, fetching Medicines ids added by customer from cookies
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        counter=medicine_ids.split('|')
        medicine_count_in_cart=len(set(counter))
    else:
        medicine_count_in_cart=1

    response = render(request, 'medicmandu/index.html',{'medicines':medicines,'medicine_count_in_cart':medicine_count_in_cart})

    #adding Medicine id to cookies
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        if medicine_ids=="":
            medicine_ids=str(pk)
        else:
            medicine_ids=medicine_ids+"|"+str(pk)
        response.set_cookie('medicine_ids', medicine_ids)
    else:
        response.set_cookie('medicine_ids', pk)

    medicine=Medicine.objects.get(id=pk)
    messages.info(request, medicine.medname + ' added to cart successfully!')

    return response



# for checkout of cart
def cartview(request):
    #for cart counter
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        counter=medicine_ids.split('|')
        Medicine_count_in_cart=len(set(counter))
    else:
        Medicine_count_in_cart=0

    # fetching Medicine details from db whose id is present in cookie
    medicines=None
    total=0
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        if medicine_ids != "":
            Medicine_id_in_cart=medicine_ids.split('|')
            medicines=Medicine.objects.all().filter(id__in = Medicine_id_in_cart)

            #for total price shown in cart
            for p in medicines:
                total=total+p.price
    return render(request,'medicmandu/cart.html',{'medicines':medicines,'total':total,'Medicine_count_in_cart':Medicine_count_in_cart})


def removefromcartview(request,pk):
    #for counter in cart
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        counter=medicine_ids.split('|')
        Medicine_count_in_cart=len(set(counter))
    else:
        Medicine_count_in_cart=0

    # removing Medicine id from cookie
    total=0
    if 'medicine_ids' in request.COOKIES:
        medicine_ids = request.COOKIES['medicine_ids']
        Medicine_id_in_cart=medicine_ids.split('|')
        Medicine_id_in_cart=list(set(Medicine_id_in_cart))
        Medicine_id_in_cart.remove(str(pk))
        Medicines=Medicine.objects.all().filter(id__in = Medicine_id_in_cart)
        #for total price shown in cart after removing Medicine
        for p in Medicines:
            total=total+p.price

        #  for update coookie value after removing Medicine id in cart
        value=""
        for i in range(len(Medicine_id_in_cart)):
            if i==0:
                value=value+Medicine_id_in_cart[0]
            else:
                value=value+"|"+Medicine_id_in_cart[i]
        response = render(request, 'medicmandu/cart.html',{'Medicines':Medicines,'total':total,'Medicine_count_in_cart':Medicine_count_in_cart})
        if value=="":
            response.delete_cookie('Medicine_ids')
        response.set_cookie('Medicine_ids',value)
        return response
