from django import forms
from .models import profile

class profileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = '__all__'