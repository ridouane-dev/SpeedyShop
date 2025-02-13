from django.urls import path
from comptes import views

urlpatterns = [
        path('',views.home , name='homme'),
        path('login',views.logIn , name='login'),
        path('register',views.register,name='register'),
        path('logout',views.logOut,name='loguot')
]