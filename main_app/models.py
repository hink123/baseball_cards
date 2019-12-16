from django.db import models
from django.urls import reverse

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    season = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.id})"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})

class Offer(models.Model):
    date = models.DateField()
    price = models.PositiveIntegerField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_price_display()} on {self.date}"