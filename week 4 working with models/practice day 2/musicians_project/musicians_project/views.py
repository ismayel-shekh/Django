from django.shortcuts import render
from album.models import AlbumModel

def Home(request):
    albums = AlbumModel.objects.all()
    return render(request, 'home.html', {'musician_albums': albums})