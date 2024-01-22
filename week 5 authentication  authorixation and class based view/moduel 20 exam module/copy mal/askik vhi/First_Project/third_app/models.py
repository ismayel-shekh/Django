from django.db import models
from second_app.models import Brand
# Create your models here.

class All_Car(models.Model):
    Car_Model = models.CharField(max_length = 100)
    Car_Details = models.TextField()
    Price = models.IntegerField()
    Brand_Name = models.ForeignKey(Brand, on_delete = models.CASCADE)
    Quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='uploads/',blank=True, null=True)

    def __str__(self) -> str:
        return self.Car_Model
    
    
    
class Comment(models.Model):
    post = models.ForeignKey(All_Car, on_delete=models.CASCADE, related_name ='comments')
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return f'Comments By {self.name}'
    