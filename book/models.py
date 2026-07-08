from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.FloatField()
    
    def __str__(self):
        return f"{self.title} by {self.author}"