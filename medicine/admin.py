from django.contrib import admin
from .models import Medicine, manufacturer
# Register your models here.
class MedicineAdmin(admin.ModelAdmin):
    pass
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(manufacturer)
