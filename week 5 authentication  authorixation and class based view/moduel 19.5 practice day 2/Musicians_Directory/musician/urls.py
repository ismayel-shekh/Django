from django.urls import path
from  . import views
urlpatterns = [
    path('', views.MusicView.as_view(), name='musicpage'),
    path('register/', views.RegisterForm.as_view(), name='registerpage'),
    path('logout/', views.LogoutForm.as_view(), name='logoutpage'),
    path('login/', views.LoginFrom.as_view(), name='loginpage'),
    path('profile/', views.profile, name = 'profilepage'),
]
