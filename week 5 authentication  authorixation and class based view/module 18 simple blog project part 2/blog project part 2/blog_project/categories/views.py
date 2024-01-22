from django.shortcuts import render, redirect
from . import forms
# Create your views here.


def add_category(request):
    if request.method == 'POST': # user post request korache
        category_form = forms.CategoryForm(request.POST) # user ar post request data ekhana captur korlam
        if category_form.is_valid(): # post kore data gula amra valid kina chack korbo 
            category_form.save() # jodi valid hoy taila database a save korbo 
            return redirect('add_category') # sob dik thakle taka add kora author url e pathya dibo 
    else: # normali webside a gela blank form paba
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html', {'form' : category_form})