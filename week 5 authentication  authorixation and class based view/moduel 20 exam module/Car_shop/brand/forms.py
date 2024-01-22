# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class RegistationForm(UserCreationForm):
#     car_brand = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))

#     class Meta:
#         model = User
#         fields =['username','car_brand',]


from django import forms
from . models import Category

class cateforyForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'