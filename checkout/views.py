from django.shortcuts import render, redirect

def Checkout(request):
    return render(request,'checkout.html')