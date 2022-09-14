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

CARDS = (
    ('border-dark', 'White'),
    ('text-white bg-primary', 'Blue'),
    ('text-white bg-secondary', 'Grey'),
    ('text-white bg-success', 'Green'),
    ('text-white bg-danger', 'Red'),
    # ('text-white bg-warning', 'Yellow'),
    ('text-white bg-info', 'Aqua'),
    # ('text-white bg-dark', 'Dark Grey')
)


class Game(models.Model):
    title = models.CharField(max_length=100, default="None")
    genre = models.CharField(max_length=100, default="None")
    min = models.CharField(max_length=100, default="None")
    max = models.CharField(max_length=100, default="None")
    length = models.IntegerField(default=0)
    image = models.CharField(max_length=1000, default="/static/06.png")
    type = models.CharField(
        max_length=30,
        choices=TYPES,
        default=TYPES[0][0]
    )
    note = models.CharField(max_length=1000, default="None")
    link = models.CharField(max_length=1000, default="None")
    color = models.CharField(
        max_length=30,
        choices=CARDS,
        default=CARDS[0][0]
    )
    cost = models.IntegerField(default=0)
    timestamp = models.DateField(auto_now_add=True)
    # Also for "owner field"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # group = models.ForeignKey(Group, on_delete=models.CASCADE)
    event = models.BooleanField(default=False)
    wishlist_user = models.BooleanField(default=False)
    coffee_group = models.BooleanField(default=False)
    hoth_group = models.BooleanField(default=False)
    gundam_group = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home_logged_in')


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