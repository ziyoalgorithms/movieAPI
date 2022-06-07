
from django.db import models


class Movie(models.Model):
    MOVIE_GENRE_CHOICES = [
        ('DRAMA', 'Drama'),
        ('KOMSEDIYA', 'Komediya'),
        ('DETIKTIV', 'Detiktiv'),
        ('ROMANTIKA', 'Romantika'),
        ('FANTASTIK', 'Fantastik'),
        ('JANGARI', 'Jangari')
    ]
    name = models.CharField(max_length=150)
    year = models.DateField()
    imdb = models.IntegerField()
    genre = models.CharField(max_length=9, choices=MOVIE_GENRE_CHOICES)
    actors = models.ManyToManyField("studio.Actor", related_name='actors', blank=True)

    def __str__ (self):
        return self.name