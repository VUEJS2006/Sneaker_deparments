from django.urls import path
from . import views

urlpatterns = [
    path('productdetail/<int:pk>', views.ProductDetail, name='productdetail'),
    path('productlist/', views.ProductList, name='productlist'),
    path('categorylist/<str:foo>', views.CategoryList, name='categorylist'),
    path('search/',views.Search_by, name='search_by'),
    

]