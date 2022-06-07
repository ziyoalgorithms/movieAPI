
from django.db import models
from studio.models.movie import Movie


class Actor(models.Model):
    ACTOR_GENDER_CHOICES = [
    ('ERKAK', 'Erkak'),
    ('AYOL', 'Ayol')
    ]
    name = models.CharField(max_length=150)
    birthdate = models.DateField()
    gender = models.CharField(max_length=5, choices=ACTOR_GENDER_CHOICES)
    movies = models.ManyToManyField(Movie, related_name='movies', blank=True)

    def __str__ (self):
        return self.name