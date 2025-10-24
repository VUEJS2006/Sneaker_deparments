from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_home, name='review_home'),
]