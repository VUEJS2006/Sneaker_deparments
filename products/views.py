from django.shortcuts import render, redirect
from .models import Product,Category
from django.contrib import messages
# Create your views here.
def ProductDetail(request, pk):
    product = Product.objects.get(id = pk)
    context = {
        'product':product
    }
    return render(request,'products_detail.html', context)

def ProductList(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'products_list.html',context)
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
    


    #  context = {
    #     'category':category
    # }
