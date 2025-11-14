from django.db import models
from django.contrib.auth.models import User

class OTP(models.Model):
    code = models.CharField(max_length=6)
    email = models.EmailField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    