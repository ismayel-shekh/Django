from django.urls import path
from .import views
urlpatterns = [   
    path('',views.Music, name ='musicpage')
]
