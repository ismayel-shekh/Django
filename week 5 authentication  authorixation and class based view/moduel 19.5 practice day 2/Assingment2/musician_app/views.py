from django.shortcuts import render,redirect
from . import forms
from . import models
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout



@method_decorator(login_required, name = 'dispatch')
class MusicView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'music.html'
    success_url = reverse_lazy ('musicpage')
    
    


class RegisterForm(CreateView):
    model = models.Musician
    form_class = forms.CreateUser
    template_name = 'register.html'
    success_url = reverse_lazy ('registerpage')


class LoginForm(LoginView):
    template_name ='register.html'
    
    
    def form_valid(self, form):
        messages.success(self.request,'Login in successfull')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,'Logged in informition was incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
    def get_success_url(self):
        return reverse_lazy ('profilepage')


@method_decorator(login_required, name = 'dispatch')
def Profile(request):
    return render(request,'profile.html')

@method_decorator(login_required, name = 'dispatch')
class LogoutForm(LogoutView):
    next_page = reverse_lazy('Homepage')
    template_name = 'home.html'
    
    
    
    
    