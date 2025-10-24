from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_read', 'created_at')
