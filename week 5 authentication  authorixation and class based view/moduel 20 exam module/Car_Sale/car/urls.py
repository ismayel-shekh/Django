from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addCarCreateView.as_view(), name='add_post'),
    # path('detail/<int:id>', views.DetailCarView.as_view(), name='detail'),
    path('details/<int:id>', views.DetailPostView.as_view(), name='detail'),
    # path('buycar/<int:id>/', views.Buycar, name='CAr_buying'),
    path('buycar/<int:id>', views.Buycar, name='Car_buying'),
]
