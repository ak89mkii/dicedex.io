from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User

# Create your models here.

TYPES = (
    ('Base Game', 'Base Game'),
    ('Expansion', 'Expansion')
)

class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    min = models.CharField(max_length=100)
    max = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    type = models.CharField(
        max_length=30,
        choices=TYPES,
        default=TYPES[0][0]
    )
    owner = models.CharField(max_length=100, default="IG88")
    note = models.CharField(max_length=1000, default="None")
    link = models.CharField(max_length=1000, default="None")
    timestamp = models.DateField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')
