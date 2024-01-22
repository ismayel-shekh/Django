from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.user_register , name='register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('profile/', views.profile, name='profile'),
    path('logout', views.LogoutView.as_view(), name='user_logout'),
    path('profile/edit_pass',views.pass_change, name='pass_change'),
    path('profile/edit_data', views.edit_profile, name='edit_profile')
]
