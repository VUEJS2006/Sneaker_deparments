
from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import Notification
from . models import Slider, Contact, Review
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def homePage(request):
    sliders = Slider.objects.all()
    c = {
        'sliders':sliders
    }
    return render(request, 'index.html',c)
def About(request):
    return render(request, 'about.html')
@login_required(login_url='login')
def UserMessage(request):
    notis = Notification.objects.filter(user = request.user, is_delete = False).order_by('-created_at')
    unread_count = notis.filter(is_read=False).count()
    context = {
        'notis':notis,
        'unread_counter':unread_count
    }
    return render(request,'message.html', context)
@login_required(login_url='login')
def ReadMessage(request, message_id):
    message = get_object_or_404(Notification, id = message_id, user = request.user)
    message.is_read = True
    message.save()
    return redirect('/sneaker_shop/messages/')
@login_required(login_url='login')
def DeleteMessage(request, message_id):
    if request.method == "POST":
        message = get_object_or_404(Notification, id = message_id, user = request.user)
        message.is_delete = True
        message.save()
        messages.error(request,'Your Notification Deleted!')
    return redirect('/messages/')
def DOC(request):
    return render(request, 'doc.html')
@login_required(login_url='login')
def ContactUs(request):
    if request.method == "GET":
     return render(request, 'contact.html')
    if request.method == "POST":
     contact  = Contact.objects.create(
        username = request.POST.get('username'),
        title = request.POST.get('title'),
        email = request.POST.get('email'),
        phone = request.POST.get('phone'),
        message = request.POST.get('message')
    )
    contact.save()
    messages.success(request,'Your Contact Successfully!')
    return redirect('/')
def PageNotFound(request):
   return render(request, '404.html')

def ReviewPage(request):
   reviews = Review.objects.all()
   context = {
      'reviews':reviews
   }
   return render(request,'review.html',context)
@login_required(login_url='login')
def ReviewCreate(request):
   if request.method ==  "GET":
      return render(request,'review.html')
   if request.method == "POST":
      review_rating = Review.objects.create(
         username = request.POST.get('username'),
         email = request.POST.get('email'),
         content_rev = request.POST.get(' content_rev'),
         rating = request.POST.get('rating'),
      )
      review_rating.save()
      messages.success(request,'Your Review Create Successfully!')
      return redirect('/')
   else:
      messages.error(request,'Please Rewrite Your Review!')
      return redirect('/sneaker_shop/review/create/')
      