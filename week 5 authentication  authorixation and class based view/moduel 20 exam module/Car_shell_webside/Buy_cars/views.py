from django.shortcuts import render
from . import forms
from . import models
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.
def history_view(request):
    history = models.car_buying_history.objects.filter(author=request.user)
    return render(request, 'history.html', {'data': history})