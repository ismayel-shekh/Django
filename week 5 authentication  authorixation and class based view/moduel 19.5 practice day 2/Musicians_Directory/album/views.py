from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
# Create your views here.

@method_decorator(login_required, name='dispatch')
class album(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('albumpage')

@method_decorator(login_required, name='dispatch')
class EditeView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    pk_url_kwarg = 'id'
    template_name = 'album.html'
    success_url = reverse_lazy('albumpage')


@method_decorator(login_required, name='dispatch')
class DeleteButton(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')