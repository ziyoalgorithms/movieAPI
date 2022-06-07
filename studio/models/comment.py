
from django.db import models
from studio.models.movie import Movie
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    
