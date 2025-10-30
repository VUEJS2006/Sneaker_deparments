from django.db import models

class Slider(models.Model):
    image = models.ImageField(upload_to='uploads/slider/')
    sli_name = models.CharField(max_length=100,  default='', blank=True, null=True)
    sli_description = models.CharField(max_length=300, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.image.name