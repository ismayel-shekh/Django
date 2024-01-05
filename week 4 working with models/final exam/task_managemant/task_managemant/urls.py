
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='showtask'),
    path('', views.font),
    path('task/', include('task.urls')),
    path('category/', include('category.urls')),
]
