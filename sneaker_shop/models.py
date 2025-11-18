from django.db import models

class Slider(models.Model):
    image = models.ImageField(upload_to='uploads/slider/')
    sli_name = models.CharField(max_length=100,  default='', blank=True, null=True)
    sli_description = models.CharField(max_length=300, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.image.name
class Contact(models.Model):
    username = models.CharField(max_length=100, null=False)
    title = models.CharField(max_length=100,null=False)
    email = models.EmailField(max_length=100, null=False)
    phone = models.CharField(max_length=100,null=False)
    message = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
class Review(models.Model):
    username = models.CharField(max_length=100,null=False)
    email = models.EmailField(max_length=100,null=False)
    content_rev = models.TextField(null=False)
    rating = models.CharField(max_length=100,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username