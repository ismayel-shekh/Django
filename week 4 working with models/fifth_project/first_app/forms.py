from django import forms
from django.core import validators


class contactForm(forms.Form):

    # widgets == fild to html input
    name = forms.CharField(label='Full Name: ', help_text="total length within 70 character", required=False, disabled=False, widget=forms.Textarea(attrs= {'id': 'text_area', 'class' : 'class1 class2', 'placeholder': 'Enter your name'}))
    file = forms.FileField()
    email = forms.EmailField(label='User Email')
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    chack = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect)
    MEAL = [('P', 'pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL,  widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Enter a name with at least 10 characters')
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")
    #     return valemail
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Enter a name with at least 10 characters')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")       

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError('Enter a value at least 10 characters')

class StudentData(forms.Form):
    name = forms.CharField( validators=[validators.MinLengthValidator(10, message='Enter a name with at least 10 characters')])
    email = forms.CharField(validators=[validators.EmailValidator(message='enter a valid email address')])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(30, message='Age must be maximum 30'), validators.MinValueValidator
    (21, message='age must be at least 21')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message='File Extension must be ended with .pdf')])

class passwordvalidationproject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confurm_password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confurm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("password destn't meatch")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")