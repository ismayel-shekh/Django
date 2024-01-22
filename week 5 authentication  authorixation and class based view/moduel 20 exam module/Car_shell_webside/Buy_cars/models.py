from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class car_buying_history(models.Model):
    Car_name = models.CharField(max_length = 100)
    Price = models.IntegerField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='uploads/',blank=True, null=True)
    Car_Details = models.TextField()
    def __str__(self):
        return self.Car_name