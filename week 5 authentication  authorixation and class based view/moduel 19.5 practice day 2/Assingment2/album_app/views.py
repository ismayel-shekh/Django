from django.shortcuts import render,redirect
from . import forms
from . import models
from django.views.generic import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name = 'dispatch')
class Album(CreateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy ('albumpage')

@method_decorator(login_required, name = 'dispatch')
class EditedView(UpdateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    pk_url_kwarg = 'id'
    template_name = 'album.html'
    success_url = reverse_lazy ('albumpage')

@method_decorator(login_required, name = 'dispatch')
class DeleteButton(DeleteView):
    model = models.AlbumModel
    template_name = 'delete.html'
    success_url = reverse_lazy('Homepage')
    pk_url_kwarg = 'id'
    