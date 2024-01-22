from django import forms
from . models import All_Car,Comment

class CarInfo(forms.ModelForm):
    class Meta:
        model = All_Car
        fields = '__all__'
        
        
class Car_comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','comment']
        