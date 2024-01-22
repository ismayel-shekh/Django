from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addCarCreateView.as_view(), name='add_post'),
    path('all', views.showdata, name='all')
]
