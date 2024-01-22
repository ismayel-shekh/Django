from django import forms
from .models import car, Comment


class carFrom(forms.ModelForm):
    class Meta:
        model = car
        fields = '__all__'

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body',]
