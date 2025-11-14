from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.homePage,name='homepage'),
    path('messages/', views.UserMessage, name='user_message'),
    path('about/',views.About, name='about'),
    path('messages/read/<int:message_id>', views.ReadMessage, name='read_message'),
    #path('messages/delete/<message_id>', views.DeleteMessage, name='message_delete'),
    path('messages/delete/<int:message_id>', views.DeleteMessage, name='delete_message'),
    path('doc/', views.DOC, name='doc'),
    path('contact/', views.ContactUs, name='contact'),
    # 404
    # re_path(r"^.*/$",views.PageNotFound, name='404error'),
    
    
    
    
]
