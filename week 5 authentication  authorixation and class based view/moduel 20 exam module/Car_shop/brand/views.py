# from django.shortcuts import render, redirect
# from . import forms
# from django.contrib import messages
# from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.views import LogoutView
# from django.urls import reverse_lazy

# # Create your views here.
# def register(request):
#     if request.method == 'POST':
#         register_form = forms.RegistationForm(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             messages.success(request, 'Account created successfully')
#             return redirect('login')
#     else:
#         register_form = forms.RegistationForm()
#     return render(request, 'register.html', {'form' : register_form ,'type': 'register'})

# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['username']
#             user_pass = form.cleaned_data['password']
#             user = authenticate(username = user_name, password = user_pass)
#             if user is not None:
#                 messages.success(request, 'Logged in successfully !')
#                 login(request, user)
#                 return redirect('login')
#             else:
#                 messages.warning(request, 'Login information incorrect')
#                 return redirect('register')
            
#     else:
#         form = AuthenticationForm()
#     return render(request, 'register.html', {'form': form, 'type': 'login'})
# class Logoutview(LogoutView):
#     def get_success_url(self):
#         return reverse_lazy('home')