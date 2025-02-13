from django.urls import path
from .views import index,checkout,confirmation

urlpatterns = [
    path('',index , name='homeB'),
    path('checkout' , checkout, name="checkout"),
    path('confirmation' , confirmation ,name="confirmation"),
]