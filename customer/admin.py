from django.contrib import admin
from .models import Customer ,Prescription
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

admin.site.register(Prescription)