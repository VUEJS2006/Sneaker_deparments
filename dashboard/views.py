from django.shortcuts import render, redirect
from products.models import Product, Category
from django.contrib.auth.models import User
from sneaker_shop.models import Slider
from django.contrib import messages
# Create your views here.
def admin_home(request):
    return render (request,'admin.html')

def CategoryList(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'admincategory.html',context)
def CategoryCreate(request):
    if request.method == "POST":
         category= Category.objects.create(
             name = request.POST.get('name'),
         )
         category.save()
         messages.info(request, 'Product Create Successfully')
    return redirect('/dashboard/admincategory/')
def CategoryUpdate(request, pk):
    category  = Category.objects.get(id = pk)
    if request.method == "POST":
        category.name = request.POST.get('name')
        category.save()
        return redirect('/dashboard/admincategory/')
def CategoryDelete(request, pk):
    category = Category.objects.get(id = pk)
    if request.method == "POST":
       category.delete()
       return redirect('/dashboard/admincategory/')
def ProductList(request):
    products = Product.objects.all()
    categorise = Category.objects.all()
    context = {
        'products':products,
        'categorise':categorise
    }
    return render(request, 'adminproduct.html', context)
def ProductCreate(request):
    if request.method == "POST":
        product = Product.objects.create(
            name = request.POST['name'],
            # name = request.POST.get('name'),
            price = request.POST['price'],
            category_id  = request.POST['category'],
            desciption = request.POST['desciption'],
            image = request.FILES.get('image'),
            is_sale = request.POST.get('is_sale') == "on",
            sale_price = request.POST['sale_price']
        )
        product.save()
        return redirect('/dashboard/adminproduct/')
    
def ProductUpdate(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.category_id = request.POST['category']
        product.desciption = request.POST['desciption']
        
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')

        product.is_sale = request.POST.get('is_sale') == "on"
        product.sale_price = request.POST['sale_price']
        
        product.save()
        return redirect('/dashboard/adminproduct/')
    
def ProductDelete(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        if product.image:
            product.image.delete()
        product.delete()
        return redirect('/dashboard/adminproduct/')
    
    return render(request, 'adminproduct.html', {'product': product})
def UserLogin(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, 'authentication.html', context)
def UserLoginDelete(request, pk):
      if request.method == "POST":
        user = User.objects.get(id = pk)
        user.delete()
        return redirect('/dashboard/authentication/')
def SliderHome(request):
     sliders = Slider.objects.all()
     context = {
         'sliders':sliders
     }
     return render(request, 'slider.html', context)
def SliderCreate(request):
    if request.method == "GET":
        return render(request, 'slidercreate.html')
    if request.method == "POST":
     slider = Slider.objects.create(
        sli_name = request.POST['name'],
        image = request.FILES.get('image'),
        sli_description = request.POST['description']
     )
     slider.save()
    return redirect('/dashboard/slider/')
def SliderUpdate(request, pk):
    slider = Slider.objects.get(id = pk)
    if request.method == "POST":
        slider.sli_name = request.POST.get('sli_name'),
        if request.FILES.get('image'):
           slider.image = request.FILES.get('image'),
        slider.sli_description = request.POST.get('sli_description'),
        slider.save()
        
    return redirect('/dashboard/slider/')
def SliderDelete(request, pk):
     slider = Slider.objects.get(id = pk)
     if request.method == "POST":
        if slider.image:
            slider.image.delete()
        slider.delete()
     return redirect('/dashboard/slider/')