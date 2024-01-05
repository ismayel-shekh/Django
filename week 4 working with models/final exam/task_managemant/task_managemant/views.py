from django.shortcuts import render
from task.models import task

def home(request):
    data = task.objects.all()
    return render(request, 'home.html', {'data': data})
def font(request):
    return render(request, 'font.html')