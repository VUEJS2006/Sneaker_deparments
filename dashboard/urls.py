from django.urls import path
from . import views 

urlpatterns = [
    path('dashboard/', views.admin_home, name='dashboard'),
    # Category
    path('admincategory/', views.CategoryList, name='admincategory'),
    path('admincategory/create/', views.CategoryCreate, name='admincategorycreate'),
    path('admincategory/update/<int:pk>', views.CategoryUpdate, name='admincategoryupdate'),
    path('admincategory/delete/<int:pk>', views.CategoryDelete, name='admincategorydelete'),
    # Products
    path('adminproduct/', views.ProductList, name='adminproduct'),
    path('adminproduct/create/', views.ProductCreate, name='adminproductcreate'),
    path('adminproduct/update/<int:pk>/', views.ProductUpdate, name="adminproductupdate"),
    path('adminproduct/delete/<int:pk>/', views.ProductDelete, name="product-delete"),
    # Authenticated
    path('authentication/', views.UserLogin,name='authentication'),
    path('authentication/delete/<int:pk>', views.UserLoginDelete, name='authentication_delete'),
    
    path('slider/', views.SliderHome, name='slider'),
    path('slider/create/', views.SliderCreate, name='slidercreate'),
    path('slider/update/<int:pk>', views.SliderUpdate, name="sliderupdate"),
    path('slider/delete/<int:pk>', views.SliderDelete, name='sliderdelete'),

    path('admin_order/', views.AdminOrder, name='admin_order'),
    path('admin_order/delete/<int:pk>', views.OrderDelete, name='order_delete'),
    path('admin_orderitem', views.OrderItems, name='admin_orderitem'),
    path('admin/status/<int:order_id>', views.OrderStatus, name='admin_status'),

]