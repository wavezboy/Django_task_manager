from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length = 255)
    description =models.TextField()
    due_date = models.DateField()
    
