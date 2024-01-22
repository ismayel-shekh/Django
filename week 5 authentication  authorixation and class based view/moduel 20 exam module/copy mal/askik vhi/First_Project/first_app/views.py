from django.shortcuts import render,redirect
from .forms import RegisterForm,ChangeForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout  
# Create your views here.

from django.contrib.auth.views import LoginView,LogoutView

def RegisterModel(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account Registerd  Successfully.')
            form.save()
    
    else:
        form = RegisterForm(request.POST)
    return render(request,'register.html',{'form':form})

@login_required
def ChangeInfo(request):
    if request.method == 'POST':
        form = ChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            messages.success(request,'Information has been changed successfully.')
            form.save()
            
            
    else:
        form = ChangeForm(instance = request.user)
    return render(request,'change_data.html',{'form':form})



class Login_Form(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('profilepage')

    def form_valid(self, form):
        messages.success(self.request,'Logged in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,'Logged in Informition is Wrong')
        return super().form_invalid(form)
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

@login_required
def Profile(request):
    return render(request,'profile.html')
            

@method_decorator(login_required, name = 'dispatch')
class LogoutForm(LogoutView):
    next_page = reverse_lazy('loginpage')
    template_name = 'login.html'