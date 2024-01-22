from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class addCarCreateView(CreateView):
    model = models.car
    form_class = forms.carFrom
    template_name  = 'add_car.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.brand = self.request.user
        return super().form_valid(form)
    

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.car
    form_class = forms.carFrom
    template_name = 'add_car.html'
    pk_url_kwarg ='id'
    success_url = reverse_lazy('profile')


@method_decorator(login_required, name='dispatch')
class DeleteCarView(DeleteView):
    model = models.car
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

def showdata(request):
    data = models.car.objects.all()
    return render(request, 'home.html', {'data': data})

class DetailCarView(DetailView):
    model = models.car
    pk_url_kwarg = 'id'