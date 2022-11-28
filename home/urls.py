from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
     #<--------- Authentication releted path / urls start here ------->
    path('sign_up',views.Auth.sign_up,name='sign_up'),
    path('sign_in',views.Auth.sign_in,name='sign_in'),
    path('sign_out',views.Auth.sign_out,name='sign_out'),
    #<--------- Authentication releted path / urls ends here ------->

   path('', views.index, name='home'),
   path('booking_info', views.booking_info, name='booking_info'),
   path('tourism', views.tourism, name='tourism'),
   path('information', views.information, name='information'),
   path('booking', views.booking, name='booking'),
   path('check_avalibility', views.check_avalibility, name='check_avalibility'),
   path('booking2', views.booking2, name='booking2'),
   # path('contactus', views.contactus, name='contactus'),
   path('MyBookings', views.MyBookings, name='MyBookings')
   
]