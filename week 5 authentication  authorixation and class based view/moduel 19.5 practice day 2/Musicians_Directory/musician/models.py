from django.db import models

# Create your models here.
from django.db import models

class Musician(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=13)
    Instrument_Type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"
