from django.urls import path
from .import views
urlpatterns = [
    path('',views.RegisterModel, name='registerPage'),
    path('login/',views.Login_Form.as_view(), name='loginpage'),
    path('profile/',views.Profile, name='profilepage'),
    path('logout/',views.LogoutForm.as_view(), name='logoutpage'),
    path('changedata/',views.ChangeInfo, name='changedatapage'),
   
]
