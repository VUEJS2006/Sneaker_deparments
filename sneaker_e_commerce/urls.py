
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('sneaker_shop.urls')),
    path('accounts/',include('accounts.urls')),
    path('cart/',include('cart.urls')),
    path('checkout/',include('checkout.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('orders/',include('orders.urls')),
    path('products/',include('products.urls')),
    path('reviews/',include('reviews.urls')),
    path('wishlist/',include('wishlist.urls')),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
