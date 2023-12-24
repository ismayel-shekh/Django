from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'author' : 'Rahim', 'age' : 5, 'lst' : ['python', 'is', 'best'], 'birthday' : datetime.datetime.now(), 'value' : '', 'courses' : [

        {
            'id' : 1,
            'name' : 'python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 6000
        },
        {
            'id' : 3, 
            'name' : 'c programming',
            'fee' : 7000
        }
    ]}
    return render(request, 'home.html', d)