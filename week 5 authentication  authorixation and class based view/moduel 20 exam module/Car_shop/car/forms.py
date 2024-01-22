from django import forms
from .models import car, Comment


class carFrom(forms.ModelForm):
    class Meta:
        model = car
        exclude = ['brand']

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body',]
