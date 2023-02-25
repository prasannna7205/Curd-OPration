from django.db import models

# Create your models here.
class DisplayData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    age=models.IntegerField()
    add=models.CharField(max_length=100)
    
