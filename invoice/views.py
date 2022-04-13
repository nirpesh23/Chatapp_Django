from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from order.models import Order
from medicine.models import Medicine
import io
# from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return
def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

# Create your views here.

@login_required (login_url='login')
@user_passes_test(is_customer)
def downloadinvoice_view(request,orderID,MedicineID):
    order=Order.objects.get(id=orderID)
    Med=Medicine.objects.get(id=MedicineID)
    mydict={
        'orderDate':order.order_date,
        'customerName':request.user,
        'customerEmail':order.email,
        'customerMobile':order.mobile,
        'shipmentAddress':order.address,
        'orderStatus':order.status,

        'productName':Med.Medname,
        'productImage':Med.Medicine_image,
        'productPrice':Med.price,
        'productDescription':Med.description,


    }
    return render_to_pdf ('Medicmandu/download_invoice.html',mydict)


