from django.urls import path
from . import views

urlpatterns = [
    path('chechout/', views.checkout_home, name='checkout_home'),
]