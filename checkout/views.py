from django.shortcuts import render, redirect
from cart.models import CartItem
from products.models import Product
from django.contrib import messages
from . models import Order, OrderItem
import random
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def Checkout(request):
    try:
        cartitems = CartItem.objects.filter(user = request.user)
    except CartItem.DoesNotExist:
        return redirect('/checkout/cart/')
    subtotal = 0
    for item in cartitems:
        subtotal += item.product.price * item.quantity
        service_fee = 3
        grand_total = subtotal + service_fee
    context = {
        'cartitems':cartitems,
        'subtotal':subtotal,
        'service_fee':service_fee,
        'grand_total':grand_total
    }

    return render(request,'checkout.html', context)
@login_required(login_url='login')
def PlaceOrder(request):
    if request.method == "POST":
     neworder = Order()
     neworder.user = request.user 
     neworder.fullname = request.POST['fullname']
     neworder.payment_method = request.POST['payment_method']
     neworder.email = request.POST['email']
     neworder.phone = request.POST['phone']
     neworder.image = request.FILES.get('image')
     neworder.address = request.POST['address']
    
     neworder.pincode = request.POST['pincode']
    
     neworder.size = request.POST['size']
     cart = CartItem.objects.filter(user = request.user)
     cart_total_price = 0
     for item in cart:
         
        cart_total_price = cart_total_price + item.product.sale_price * item.quantity
        neworder.total_price = cart_total_price
        neworder.save()
     neworderitem = CartItem.objects.filter(user = request.user)
     for item in neworderitem:
         OrderItem.objects.create(
            order = neworder,
            product = item.product,
            price = item.product.sale_price,
            quantity = item.quantity 
         )
        #  orderproduct = Product.objects.filter(id = item.product.id).first()
        #  orderproduct.quantity = orderproduct.quantity - item.quantity
        #  orderproduct.save()
         CartItem.objects.filter(user=request.user).delete()
         messages.success(request, 'Order Successfully!')
    return redirect('/')