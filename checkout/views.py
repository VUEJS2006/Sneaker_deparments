from django.shortcuts import render

# Create your views here.
def checkout_home(request):
    return render(request,'checkout_home.html')