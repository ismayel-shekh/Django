from django import forms 
from django.core import validators
from django.forms.widgets import NumberInput
import datetime





Birthday_choices = ['2000','2001', '2002', '2003', '2004']

class contactform(forms.Form):
    name = forms.CharField(label = 'Full name: ', help_text='must be included')

    comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField(widget=NumberInput(attrs={'type' : 'date'}))
    Birthday = forms.DateField(widget=forms.SelectDateWidget(years=Birthday_choices))
    value = forms.DecimalField()
    email_next = forms.EmailField(required=False,)
    email_address = forms.EmailField(label="please enter your email address")
    day = forms.DateField(initial=datetime.date.today)
    favorite= [('blue', 'Blue'), 
               ('green', 'Green'),
               {'black', 'Black'},
               ]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect,choices=favorite)
    color = forms.MultipleChoiceField(choices=favorite)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=favorite)
    password = forms.CharField(widget=forms.PasswordInput())