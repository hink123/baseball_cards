from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    season = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.id})"
    
