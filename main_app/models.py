from django.db import models
from django.urls import reverse

# Create your models here.

POSITIONS = (
    ('P', 'Pitcher'),
    ('C', 'Catcher'),
    ('1B', 'First Base'),
    ('2B', 'Second Base'),
    ('3B', 'Third Base'),
    ('SS', 'Short Stop'),
    ('LF', 'Left Field'),
    ('CF', 'Center Field'),
    ('RF', 'Right Field'),
    ('DH', 'Designated Hitter')
)

class Card(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    position = models.CharField(
        max_length=2,
        choices=POSITIONS,
    )
    season = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.id})"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})

class Offer(models.Model):
    date = models.DateField('Date Offered')
    price = models.PositiveIntegerField('Bid')
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"${self.price} on {self.date}"
    
    class Meta:
        ordering = ['-price']