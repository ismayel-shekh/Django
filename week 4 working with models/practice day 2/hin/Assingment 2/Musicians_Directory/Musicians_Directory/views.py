# from django.shortcuts import render
# from musician_app.models import Musician
# from album_app.models import AlbumModel
# def Home(request):
#     data = Musician.objects.all()
#     album =AlbumModel.objects.all()
#     return render(request,'home.html',{'data':data},{'album':album})

from django.shortcuts import render
from musician_app.models import Musician
from album_app.models import AlbumModel

def Home(request):
    

    albums = AlbumModel.objects.all()
    return render(request, 'home.html', {'musician_albums': albums})