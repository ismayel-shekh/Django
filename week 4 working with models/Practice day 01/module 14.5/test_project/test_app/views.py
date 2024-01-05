from django.shortcuts import render
from . froms import contactform
from . import models
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form = contactform()
    else:
        form = contactform()
    return render(request, './home.html', {'form' : form})


def model_home(request):
    test_model = models.test_model.objects.all()
    print(test_model)
    return  render(request, 'model.html', {'data': test_model})