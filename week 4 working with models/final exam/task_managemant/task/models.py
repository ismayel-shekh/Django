from django.db import models
from category.models import catagory
# Create your models here.
class task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_complete = models.BooleanField(default=False)
    Task_Assign_Date = models.DateField()
    catagory = models.ManyToManyField(catagory)

    def __str__(self):
        return self.taskTitle


