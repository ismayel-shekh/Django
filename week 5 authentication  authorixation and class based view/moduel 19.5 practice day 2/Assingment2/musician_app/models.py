
from django.db import models

class Musician(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=25)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=14)
    Instrument_Type = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"
