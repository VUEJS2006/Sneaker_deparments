from django.db import models

# Create your models here.
import datetime
class Category(models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
   return self.name
  class Meta:
    verbose_name_plural = 'categories'

class Product(models.Model):
   name = models.CharField(max_length=100)
   price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
   category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
   desciption = models.CharField(max_length=300, default='', blank=True, null=True)
   image = models.ImageField(upload_to='uploads/product/')
   is_sale = models.BooleanField(default=False)
   sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
   def __str__(self):
     return self.name
