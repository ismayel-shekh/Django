from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm ,  PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
# Create your views here.
def user_register(request):
    if request.method == 'POST':
        register_form = forms.RegistationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'account created successfully')
            return redirect('register')
    else:
        register_form = forms.RegistationForm()
    return render(request, 'register.html', {'form': register_form, 'type': 'register'})


class UserLoginView(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Login successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Login failed')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['type'] = 'Login'
        return context

class LogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('user_login')

# class UserLogoutView(View):
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect(reverse_lazy('user_login'))

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'password change successful')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form': form})

@login_required
def profile(request):
    # data =User.objects.all()
    data = request.user
    return render(request, 'profile.html', {'data': data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserform(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserform(instance = request.user)

    return render(request, 'update_profile.html', {'form': profile_form})