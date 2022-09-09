from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, Group

# Create your models here.

TYPES = (
    ('Base Game', 'Base Game'),
    ('Expansion', 'Expansion')
)

COLORS = (
    ('Dark', 'Dark'),
    ('Light', 'Light')
)


class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    min = models.CharField(max_length=100)
    max = models.CharField(max_length=100)
    length = models.IntegerField()
    image = models.CharField(max_length=1000)
    type = models.CharField(
        max_length=30,
        choices=TYPES,
        default=TYPES[0][0]
    )
    note = models.CharField(max_length=1000, default="None")
    link = models.CharField(max_length=1000, default="None")
    timestamp = models.DateField(auto_now_add=True)
    # Also for "owner field"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # group = models.ForeignKey(Group, on_delete=models.CASCADE)
    coffee_group = models.BooleanField(default=True)
    hoth_group = models.BooleanField(default=True)
    gundam_group = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('groups')


class Theme(models.Model):
    color = models.CharField(
        max_length=30,
        choices=COLORS,
        default=COLORS[1][1]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.color

    def get_absolute_url(self):
        return reverse('home_logged_in')