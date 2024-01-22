from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('detail/<int:id>/',views.DetailPostview.as_view(), name='detialpage'),
    path('buycar/<int:id>/',views.BuyCar,name='buycarpage')
]