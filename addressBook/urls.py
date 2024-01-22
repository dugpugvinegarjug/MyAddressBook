from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addressList', views.addressList, name='addressList'),
    path('addAddress', views.addAddress, name='addAddress'),
]


