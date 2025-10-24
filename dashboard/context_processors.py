from .models import Notification
def unread_count(request):
    if request.user.is_authenticated:
        count = Notification.objects.filter(user = request.user, is_read = False, is_delete = False).count()
    else:
        count = 0
    return {'unread_count':count}