from django import forms
from .models import Musician
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        
        
class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']