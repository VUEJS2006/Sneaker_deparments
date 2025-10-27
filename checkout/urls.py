from django.urls import path
from . import views

urlpatterns = [
    path('chechout/', views.Checkout, name='checkout'),
    
]