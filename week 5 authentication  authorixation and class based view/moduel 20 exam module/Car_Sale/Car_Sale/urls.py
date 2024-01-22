from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("category/<str:Brand>/",views.showdata, name="category_wice_car"),
    path('', views.showdata, name='homepage'),
    path('car/', include('car.urls')),
    path('author/', include('author.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)