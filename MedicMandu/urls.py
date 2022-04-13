"""MedicMandu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from contactuspage.views import contactus_view
from about.views import about_view , about_Pharmacist , about_Pharmacy
from pharmacy.views import home_view , afterlogin_view , search_view,payment_success_view

from django.contrib.auth.views import LoginView,LogoutView
from customer.views import user_signup_view , user_home_view , profileview ,useraddressview, useraddressview2
from admin.views import admin_dashboard_view , viewcustomer ,updatecustomer ,adminmedicineview ,deletecustomer
from order.views import order_view 
from cart.views import cartview ,addtocartview , removefromcartview
from invoice.views import downloadinvoice_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactus/',contactus_view ,name='contactus' ),
    path('aboutus/', about_view,name='aboutus'),
    path('aboutpharmacist/', about_Pharmacist,name='aboutpharmacist'),
    path('aboutpharmacy/', about_Pharmacy,name='aboutpharmacy'),
    path('afterlogin/', afterlogin_view,name='afterlogin'),
    path('', home_view , name = 'home'),
    path('search', search_view,name='search'),
    path('usersignup', user_signup_view,name='signup'),
    path('userlogin', LoginView.as_view(template_name='medicmandu/login.html'),name='login'),
    path('user-home', user_home_view,name='user-home'),

    path('logout/', LogoutView.as_view(template_name='medicmandu/logout.html'),name='logout'),


    path('addtocart/<int:pk>', addtocartview,name='addtocart'),
    path('cart', cartview,name='cart'),
    path('removefromcart/<int:pk>', removefromcartview,name='removefromcart'),

     path('admin-dashboard', admin_dashboard_view,name='admin-dashboard'),

    path('order', order_view,name='order'),
    path('profile', profileview,name='profile'),
    path('downloadinvoice/<int:orderID>/<int:MedicineID>', downloadinvoice_view,name='downloadinvoice'),

    path('useraddress', useraddressview,name='useraddress'),
    path('useraddress2', useraddressview2,name='useraddress2'),
    path('payment-success', payment_success_view,name='payment-success'),
    
    
    path('viewcustomer', viewcustomer,name='view-customer'),
    path('deletecustomer/<int:pk>', deletecustomer,name='deletecustomer'),
    path('updatecustomer/<int:pk>', updatecustomer,name='updatecustomer'),

    path('adminmedicines', adminmedicineview,name='admin-products'),
    # path('admin-add-product', views.admin_add_product_view,name='admin-add-product'),
    # path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    # path('update-product/<int:pk>', views.update_product_view,name='update-product'),

    # path('admin-view-booking', views.admin_view_booking_view,name='admin-view-booking'),
    # path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
    # path('update-order/<int:pk>', views.update_order_view,name='update-order'),


    
    
    ]



