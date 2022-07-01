from django.urls import path, include
from rest_framework import routers

from .views import PaymentViewSet , OrderViewSet , manufacturerViewSet , MedicineViewSet , ReturnMedicineViewSet , CustomerViewSet , PrescriptionViewSet
router = routers.DefaultRouter()
router.register(r'PaymentViewSet',PaymentViewSet)
router.register(r'OrderViewSet',OrderViewSet)
router.register(r'ReturnMedicineViewSet',ReturnMedicineViewSet)
router.register(r'manufacturerViewSet',manufacturerViewSet)
router.register(r'CustomerViewSet',CustomerViewSet)
router.register(r'PrescriptionViewSet',PrescriptionViewSet)
router.register(r'MedicineViewSet',MedicineViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

