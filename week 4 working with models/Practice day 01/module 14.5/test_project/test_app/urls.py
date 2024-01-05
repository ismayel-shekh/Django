from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('model/', views.model_home, name = 'homemodel')
]
