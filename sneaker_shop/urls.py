from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage,name='homepage'),
    path('messages/', views.UserMessage, name='user_message'),
    path('about/',views.About, name='about'),
    path('messages/read/<int:message_id>', views.ReadMessage, name='read_message'),
    #path('messages/delete/<message_id>', views.DeleteMessage, name='message_delete'),
    path('messages/delete/<int:message_id>', views.DeleteMessage, name='delete_message'),
]
