from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.FloatField()
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Task(models.Model):
    title = models.CharField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    