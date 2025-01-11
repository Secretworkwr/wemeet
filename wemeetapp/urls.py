from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('home/',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('chat/',views.message_page,name="chat"),
    path('neon/',views.chatbot,name='neon'),
    path('home/',views.return_home,name='home'),
    path('api',views.chatapi,name='chatapi'),
    path('vcall/',views.vcall,name='vcall'),
    path('meeting/',views.videocall,name='meeting'),
    path('join/',views.join_room,name='join'),
    
]