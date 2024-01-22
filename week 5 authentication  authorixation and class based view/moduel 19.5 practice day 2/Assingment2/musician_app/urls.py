from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    
    path('',views.MusicView.as_view(), name ='musicpage'),
    path('regiser/',views.RegisterForm.as_view(), name ='registerpage'),
    path('login/',views.LoginForm.as_view(), name ='loginpage'),
    path('logout/',views.LogoutForm.as_view(), name ='logoutpage'),
    path('profile/',views.Profile, name ='profilepage'),
]
