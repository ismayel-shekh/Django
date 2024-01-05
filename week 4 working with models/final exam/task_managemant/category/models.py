from django.db import models

# Create your models here.

class catagory(models.Model):
    Category_Name = models.CharField(max_length=100)


    def __str__(self):
        return self.Category_Name