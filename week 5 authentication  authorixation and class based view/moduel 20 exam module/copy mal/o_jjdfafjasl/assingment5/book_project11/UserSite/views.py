from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . forms import PostForm,UserProfileForm
from .models import PostModel,Userprofile,Borrow_History
from django.views.generic import DetailView
from django.utils import timezone
from datetime import datetime
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

def send_transaction_email(user, amount, subject, template):
    message = render_to_string(template,{
        'user': user,
        'amount':amount,
    })
    send_email = EmailMultiAlternatives(subject,'', to= [user.email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()



def Registerview(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)
            messages.success(request, 'Account Registerd successfully')
           
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


class Loginformview(LoginView):
    template_name = 'register.html'
    
    
    def get_success_url(self):
        return reverse_lazy('profilepage')
    
    def form_valid(self, form):
        messages.success(self.request, 'Login successfully')
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.success(self.request, 'Invalid Username or Password')
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
@method_decorator(login_required, name='dispatch')
class Logoutformview(LogoutView):
    template_name = 'register.html'
    next_page = reverse_lazy('homepage')


@login_required
def Profileview(request):
    
    data = Borrow_History.objects.filter(user = request.user)
    return render(request,'profile.html', {'data' : data})


@login_required
def AddPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) 
            post.author = request.user
            post.save()
            return redirect('addpostpage')
    else:
        form = PostForm()
    return render(request, 'addspost.html', {'form': form})


class DetailPage(DetailView):
    model = PostModel
    pk_url_kwarg = 'id'
    template_name = 'detials.html'
    context_object_name = 'usersite'


@login_required
def DepositeView(request):
    user_account = request.user.account
    print(user_account)
    
    if request.method == 'POST':
        form =UserProfileForm(request.POST)
        
        if form.is_valid():
            deposite_amount = form.cleaned_data['amount']
            user_account.amount += deposite_amount
            user_account.save()
            send_transaction_email(request.user, deposite_amount, 'Deposite Message', 'deposite_email.html')
            
            return redirect('depositepage')
        
    else:
        form = UserProfileForm()
    return render(request, 'deposit.html', {'form': form})



@login_required
def borrow_book(request, id):
    
    usersite = PostModel.objects.get(id=id)
    user_profile = Userprofile.objects.get(user=request.user)
    if usersite.Book_Quantity > 0:
        if user_profile.amount >= usersite.browing_price:
            user_profile.amount -= usersite.browing_price
            user_profile.save()
            
            borrow_history = Borrow_History(
            user=request.user,
            book=usersite,
            borrow_time=timezone.now(),
            )
            borrow_history.save()
            send_transaction_email(request.user, usersite.browing_price, 'Book Borrow Price', 'buybook.html')
            messages.success(request,'Book purchased Successfully')
            
        else:
            messages.success(request,'Your account not enough balance to purchase of this book !')
            
        usersite.Book_Quantity -= 1
        usersite.save()
        
    else:
        messages.error(request,'This Book not abailable in our stock')
        
    return render(request, 'detials.html', {'usersite': usersite})
    
    