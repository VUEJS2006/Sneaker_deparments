from django.shortcuts import render
from checkout.models import Order, OrderItem

# Create your views here.
def order_list(request):
    user_orders = OrderItem.objects.filter(order__user = request.user)
    context = {
        'user_orders':user_orders
    }
    return render(request,'order_list.html', context)
