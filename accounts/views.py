from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def LoginView(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect('/dashboard/dashboard/')
            else:
                return redirect('/')
        return render(request, "login.html")

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            messages.error(request, "Email not found")
            return redirect('/accounts/login/')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/dashboard/dashboard/')
            else:
                return redirect('/')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('/accounts/login/')


def RegisterView(request):
    if request.method == "GET":
        return render(request,"register.html")
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if User.objects.filter(username = username):
            messages.error(request, "Username already exists")
            return redirect('/accounts/register/')
        if User.objects.filter(email = email):
            messages.error(request, "email already exists")
            return redirect('/accounts/register/')
        if password == password_confirm:
            user = User.objects.create_user(
            username=username,
            email=email,
            password=password
            )  
            user.save()
            login(request,user)
            messages.success(request,"Register successfully")
            return redirect('/accounts/login/')
        else:
            messages.error(request,"Password does not match")
            return redirect('/accounts/register/')
def LogoutView(request):
    logout(request)
    return redirect('/accounts/login/')

def ChangePasswrd(request):
    user = request.user
    if request.method == "GET":
      return render(request, 'change_password.html',{'user':user})
    if request.method == "POST":
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not user.check_password(current_password):
            messages.error(request, 'Your Current Password is wrong!')
            return redirect('/accounts/change/password/')
        elif new_password != confirm_password:
            messages.error(request, 'Your Password Does Not Match!')
            return redirect('/accounts/change/password/')
        elif new_password == current_password:
            messages.error(request, 'Your Current Password and New Password Is Same!')
            return redirect('/accounts/change/password/')
        else:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Your Change Password Success!')
            return redirect('/accounts/login/')


   