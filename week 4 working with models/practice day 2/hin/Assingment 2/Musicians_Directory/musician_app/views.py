from django.shortcuts import render,redirect
from . import forms
# Create your views here.

def Music(request):
    if request.method =="POST":
        music_form = forms.MusicianForm(request.POST)
        if music_form.is_valid():
            music_form.save()
            return redirect('musicpage')
            
    else:
        music_form = forms.MusicianForm
    return render(request,'music.html',{'form':music_form})

    