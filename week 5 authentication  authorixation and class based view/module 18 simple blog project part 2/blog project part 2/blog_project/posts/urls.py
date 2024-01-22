from django.urls import path
from . import views  
urlpatterns = [
    path('add/', views.add_Post, name='add_Post'),
    path('edit/<int:id>', views.edit_Post, name='edit_Post'),
    path('delete/<int:id>', views.delete_post, name='delete_Post'),
]
