from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    car_name = models.CharField(max_length=50)
    car_detail = models.TextField()
    car_price = models.IntegerField()
    car_quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # ekta post multiple categorir moddhe thakte pare abar ekta categorir moddhe multiple post thakte pare
    image = models.ImageField(upload_to='posts/media/uploads/', blank = True, null = True)
    def __str__(self):
        return self.car_name
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # jkhn e ei class er object toiri hobe sei time ta rekhe dibe
    
    def __str__(self):
        return f"Comments by {self.name}"
        
    