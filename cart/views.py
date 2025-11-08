from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from products.models import Product
from . models import CartItem
import json

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product , id=product_id)

    # quantity from POST, fallback 1
    if request.method == "POST":
        try:
            qty = int(request.POST.get("quantity", 1))
        except (TypeError, ValueError):
            qty = 1
    else:
        qty = 1

    qty = max(1, min(qty, 100))

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': qty}
    )

    if not created:
        cart_item.quantity += qty
        cart_item.save()

    messages.success(request, f"Added {qty} * {product.name} to cart.")
    return redirect('cart')


@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user).select_related('product')
    cart_subtotal = sum([item.total_price for item in cart_items], Decimal('0.00'))
    # service_fee = Decimal('3.00') if cart_subtotal > 0 else Decimal('0.00')
    cart_total = cart_subtotal
    #  + service_fee

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'cart_subtotal': cart_subtotal,
        'cart_total': cart_total,
    })


@login_required
def update_cart(request,):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            item_id = data.get('item_id')
            quantity = int(data.get('quantity', 1))
        except:
            return JsonResponse({"success": False})

        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)

        if quantity <= 0:
            cart_item.delete()
            item_total = 0
        else:
            cart_item.quantity = quantity
            cart_item.save()
            item_total = cart_item.total_price

        cart_items = CartItem.objects.filter(user=request.user)
        cart_subtotal = sum([item.total_price for item in cart_items])
        service_fee = 3.00 if cart_subtotal > 0 else 0
        cart_total = cart_subtotal + service_fee

        return JsonResponse({
            "success": True,
            "item_total": item_total,
            "cart_subtotal": cart_subtotal,
            "cart_total": cart_total
        })

    return JsonResponse({"success": False})


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, f"Removed {cart_item.product.name} from cart.")
    return redirect('cart')
