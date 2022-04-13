from django.shortcuts import render

# Create your views here.
def about_view(request):
    return render(request,'medicmandu/aboutus.html')

def about_Pharmacist(request):
    return render(request,'medicmandu/aboutpharmacist.html')

def about_Pharmacy(request):
    return render(request,'medicmandu/aboutpharmacy.html')