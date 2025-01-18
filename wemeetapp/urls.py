from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('home/',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('chat/',views.message_page,name="chat"),
    
    path('home/',views.return_home,name='home'),
    
    path('vcall/',views.vcall,name='vcall'),
    path('meeting/',views.videocall,name='meeting'),
    path('join/',views.join_room,name='join'),
    path('neon/', views.chatbot_page, name='chatbot_page'),
    path('chatbot/', views.chatbot_view, name='chatbot'), 
   
    
]