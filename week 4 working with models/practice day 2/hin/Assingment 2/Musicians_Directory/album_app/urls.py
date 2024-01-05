from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.Album, name='albumpage'),
    path('edited/<int:id>',views.Edited, name='editedbutton'),
    path('deleted/<int:id>',views.DeleteButton, name='deletebutton')
]