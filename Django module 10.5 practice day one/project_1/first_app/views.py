from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    x = {'name' : 'ismayel', 'age' : 20, 'lst' : ['May', 'i', 'coming', '?'],'test' : ' ','space' : 'Well come to py thon ', 'date' : datetime.datetime.now(),
         
         'options' : [
            { 'op' : 1,
             'name' : 'Ismayel',
             'courses' : 'python'
             },
            {
                'op' : 2,
                'name' : 'hasan',
                'course' : 'programming hero',
            }
         ]
         }
    return render(request, 'home.html', x)
def final(request):
    return HttpResponse("hello walcome to fist_app home page")