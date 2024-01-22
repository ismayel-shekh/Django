from django.db import models
from musician_app.models import Musician

class AlbumModel(models.Model):
    Album_name = models.CharField(max_length=30)
    ReleaseDate = models.DateField()
    int_choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    Rating = models.PositiveSmallIntegerField(choices=int_choices)
    First_Name = models.ForeignKey(Musician, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.Album_name

    