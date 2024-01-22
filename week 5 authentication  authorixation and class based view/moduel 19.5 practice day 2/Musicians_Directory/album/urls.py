from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.album.as_view(), name='albumpage'),
    path('edited/<int:id>', views.EditeView.as_view(), name='editedbutton'),
    path('delete/<int:id>', views.DeleteView.as_view(), name='deletebutton')
]
