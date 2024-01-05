from django.shortcuts import render,redirect
from .import forms
from . import models
# Create your views here.

def Album(request):
    if request.method =="POST":
        album_forms = forms.AlbumForm(request.POST)
        if album_forms.is_valid():
            album_forms.save()
            return redirect('albumpage')
            
    else:
        album_forms = forms.AlbumForm
    return render(request,'album.html',{'form':album_forms})


def Edited(request,id):
    album = models.AlbumModel.objects.filter(pk = id).first()
    if request.method =="POST":
        album_forms = forms.AlbumForm(request.POST,instance=album)
        if album_forms.is_valid():
            album_forms.save()
            return redirect('albumpage')
    else:
        
        album_forms = forms.AlbumForm(instance=album)
    return render(request,'album.html',{'form':album_forms})

    
def DeleteButton(request,id):
     album = models.AlbumModel.objects.filter(pk = id)
     album.delete()
     return redirect('Homepage')