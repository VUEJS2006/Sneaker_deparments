from django.shortcuts import render, redirect
from .models import Product,Category
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def ProductDetail(request, pk):
    product = Product.objects.get(id = pk)
    context = {
        'product':product
    }
    return render(request,'products_detail.html', context)
@login_required(login_url='login')
def ProductList(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'products_list.html',context)
@login_required(login_url='login')
def CategoryList(request, foo):
    foo  = foo.replace('_', '')
    try:
     category = Category.objects.get(name = foo)
     products = Product.objects.filter(category = category)
     context = {
        'category':category,
        'products':products
     }
     return render(request, 'category.html', context)
    except:
        messages.success(request, ("That Category Doesn't exists"))
        return redirect('/')    
def Search_By(request):
   if request.method == "GET":
    keyword = request.GET.get('keyword','')
    products = Product.objects.all()
    product_count = products.count()

   if keyword:
      products = products.filter(Q(name__icontains = keyword) | Q(price__icontains = keyword))
      product_count = products.count()
      context = {
       'products':products,
       'product_count':product_count
       }
   return render(request, 'products_list.html', context)