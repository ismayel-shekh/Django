from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='Homepage'),
    path('musicpage/', include('musician.urls')),
    path('albmpage/', include('album.urls'))
]

