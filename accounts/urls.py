from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView, name='login'),
    path('register/', views.RegisterView, name='register'),
    path('logout/', views.LogoutView, name='logout'),
    path('change/password/',views.ChangePasswrd, name='change_pass'),   
    path('email_confirm/', views.EmailConfirm, name='email_comfirm'),
    path('otp/<str:email>', views.OTPSend, name='otp'),
    path('reset_password/<str:email>', views.ResetPassword, name='reset_pass'),
]
