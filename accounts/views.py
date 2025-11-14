from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User 
from . models import OTP
from django.contrib.auth.decorators import login_required
from random import randrange
from django.conf import settings
from django.core.mail import send_mail
def generate_random_code():
    random_code = randrange(1000, 9999)
    return random_code
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

def EmailConfirm(request):
    if request.method == "GET":
        return render(request, 'email_confirm.html')
    if request.method == "POST":
        email = request.POST.get('email')

        if User.objects.filter(email = email).exists():
            otp = OTP.objects.create(code = generate_random_code(),email=email)
            subject = "OTP code For U!"
            message = f"Your OTP code is{otp.code}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject,message,email_from,recipient_list)
            return redirect(f'/accounts/otp/{email}')
        else:
            messages.error(request, 'Email Not Found!')
            return redirect('/accounts/email_confirm/')
def OTPSend(request, email):
    if request.method == "GET":
        user = User.objects.filter(email = email).first()
        if user:
            context = {
                'email':email
            }
            return render(request,'otp.html',context)
        else:
            messages.error(request,'User Not Found!')
            return redirect('/accounts/email_confirm/')
    if request.method == "POST":
        code = request.POST.get('code')
        code_verify = OTP.objects.filter(email = email).latest('-created_at')
        otp_code = code_verify.code
        if code == otp_code:
         code_verify.delete()
         messages.success(request,'OTP Verified Success!')
         return redirect(f'/accounts/reset_password/{email}')
        else:
            messages.error(request,'OTP Not Found!')
            return redirect(f'/accounts/otp/{email}')
def ResetPassword(request, email):
    user = User.objects.get(email = email)
    if request.method == "GET":
     context = {
         'user':user
     }
     return render(request,'reset_pass.html',context) 
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request,'Your Email Not Found!')
            return redirect(f'/accounts/reset_password/{email}')
        else:
           user.set_password(password)
           user.save()
           messages.success(request,'Your Reset Password is Successfully!')
           return redirect('/accounts/login/')