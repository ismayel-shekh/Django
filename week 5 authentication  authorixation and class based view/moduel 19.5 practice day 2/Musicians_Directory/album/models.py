from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    release_date = models.DateField()
    choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    Rating = models.PositiveSmallIntegerField(choices=choices)
    writer = models.ForeignKey(Musician, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.album_name