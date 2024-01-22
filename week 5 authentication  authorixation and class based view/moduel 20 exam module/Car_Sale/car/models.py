from django.db import models
from django.contrib.auth.models import User
from brand.models import Category


# Create your models here.
class car(models.Model):
    car_image = models.ImageField(upload_to='car/media/uploads/')
    # image = models.ImageField(upload_to='posts/media/uploads/', blank=True, null=True) # actual line
    car_Name = models.CharField(max_length=50)
    car_price = models.IntegerField(default=0)
    car_quentiry = models.PositiveIntegerField(default=0)
    car_detail = models.TextField()
    brand_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_Name


class Comment(models.Model):
    car = models.ForeignKey(
        car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField(default=None)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comment by {self.name}'
