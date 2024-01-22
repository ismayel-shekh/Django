from django import forms
from .models import car_buying_history

class history(forms.ModelForm):
    class Meta:
        model = car_buying_history
        fields = '__all__'