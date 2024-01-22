from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class CategoryModel(models.Model):
    category = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 100, blank = True, null = True, unique = True)
    def __str__(self):
        return self.category
    

class PostModel(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    category = models.ManyToManyField(CategoryModel)
    browing_price = models.IntegerField()
    Book_Quantity = models.IntegerField(blank = True, null = True)
    image = models.ImageField(upload_to= 'UserSite/media/uploads/', blank=True, null= True)
    
    
    def __str__(self):
        return self.title
    
class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name = 'account', on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)   
    
    
    def __str__(self):
        return str(self.user.username) 
    
    


class Borrow_History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    borrow_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} - {self.book.title} - {self.borrow_time}"