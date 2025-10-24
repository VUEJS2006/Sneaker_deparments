
from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import Notification
def homePage(request):
    return render(request, 'index.html')
def About(request):
    return render(request, 'about.html')
def UserMessage(request):
    messages = Notification.objects.filter(user = request.user, is_delete = False).order_by('-created_at')
    unread_count = messages.filter(is_read=False).count()
    context = {
        'messages':messages,
        'unread_counter':unread_count
    }
    return render(request,'message.html', context)
def ReadMessage(request, message_id):
    message = get_object_or_404(Notification, id = message_id, user = request.user)
    message.is_read = True
    message.save()
    return redirect('/sneaker_shop/messages/')
def DeleteMessage(request, message_id):
    if request.method == "POST":
        message = get_object_or_404(Notification, id = message_id, user = request.user)
        message.is_delete = True
        message.save()
    return redirect('/messages/')
    
