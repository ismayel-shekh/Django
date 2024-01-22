from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.Album.as_view(), name='albumpage'),
    path('edited/<int:id>',views.EditedView.as_view(), name='editedbutton'),
    path('deleted/<int:id>',views.DeleteButton.as_view(), name='deletebutton')
]