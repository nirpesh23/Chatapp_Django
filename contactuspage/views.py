from django.conf import settings
from django.shortcuts import render
from . import forms,models
from django.core.mail import send_mail

# Create your views here.
def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            phone=sub.cleaned_data['Phone']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message, settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'medicmandu/contactussuccess.html')
    return render(request, 'medicmandu/contactus.html', {'form':forms.ContactusForm})


