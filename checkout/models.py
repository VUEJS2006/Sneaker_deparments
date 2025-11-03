from django.db import models
from products.models import Product
from django.contrib.auth.models import User
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    size = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100,null=False)
    address = models.TextField(null=False)
    city = models.TextField(max_length=100, null=False)
    state = models.TextField(max_length=100, null=False)
    country = models.TextField(max_length=100, null=False)
    pincode = models.CharField(max_length=100, null=False)
    total_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='uploads/checkout/')
    payment_choices =[
        ('KPay','KPay'),
        ('Wave Money', 'Wave Money'),
        ('Yoma Pay','Yoma Pay'),
        ('AYA Pay','AYA Pay'),
        ('UAB Pay', 'UAB Pay'),
    ] 
    payment_method = models.CharField(max_length=20,choices=payment_choices,default='kpay')
    order_status = [
        ('Pending','Pending'),
        ('Cancel','Cancel'),
        ('Complete','Complete'),
    ]
    status = models.CharField(max_length=100, choices=order_status,default='Pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)

class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{} {}'.format(self.order.id, self.order.tracking_no) 


