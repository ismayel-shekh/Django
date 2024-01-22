from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CategoryModel, PostModel,Borrow_History

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
       model = CategoryModel
       fields = '__all__'
       
       
class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title','description','category','browing_price','Book_Quantity','image']
        
class UserProfileForm(forms.Form):
    amount = forms.DecimalField()
        
        

class BorrowHistoryForm(forms.ModelForm):
    class Meta:
        model = Borrow_History
        fields = ['user', 'book', 'borrow_time', ]
