from django.shortcuts import render

# Create your views here.
def wishlist_home(request):
    return render(request, 'wishlist_home.html')