from django import forms
from .models import AlbumModel

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'
        widgets = {
            'ReleaseDate':forms.DateInput(attrs={'type': 'date'}),
            
        }