from django.urls import path
from . import views




urlpatterns=[
    path('',views.index,name="home"),
    path('save_livreur/', views.save_livreur, name='save_livreur'),
    path('dashboard', views.dashboard , name="dashboard"),
    path('assign_livraison/', views.assign_livraison, name='assign_livraison'),
    path('client_dashboard/', views.client_dashboard, name='client_dashboard'),
    path('confirm_reception/', views.confirm_reception, name='confirm_reception'),
    path('rate_service/', views.rate_service, name='rate_service'),
    path('com', views.com , name='com')
]