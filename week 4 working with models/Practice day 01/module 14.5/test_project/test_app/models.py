from django.db import models

# Create your models here.
class test_model(models.Model):
    auto_field = models.AutoField(primary_key=True)
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to='files/')

    def __str__(self) -> str:
        return f"auto_field: {self.auto_field}"