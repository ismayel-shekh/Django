from django import forms
from first_app.models import StudentModel

class StudentFrom(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # exclude = ['roll',]
        labels = {
            'name' : 'student Name',
            'roll' : 'student Roll'
        }
        widgets = {
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name' : "write your full name"
        }
        error_massage ={
            'name' : {'requeired' : 'your name must be reqired'}
        }