from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Registerview, name = 'registerpage'),
    path('profile/',views.Profileview, name = 'profilepage'),
    path('login/',views.Loginformview.as_view(), name = 'loginpage'),
    path('logout/',views.Logoutformview.as_view(), name = 'logoutpage'),
    path('addpost/',views.AddPost, name = 'addpostpage'),
    path('userhtml/details/<int:id>/', views.DetailPage.as_view(), name='detailpage'),
    path('posite/', views.DepositeView, name='depositepage'),
    path('borrowBook/<int:id>/', views.borrow_book, name='borrowbookpage'),
    
    
]