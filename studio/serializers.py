
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import Actor, Movie, Comment
import datetime


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'birthdate', 'gender', 'movies')


    def validate_birthdate(self, value):
        if value < datetime.date(1950, 1, 1):
            raise ValidationError(detail="1950.01.01 dan yuqori sanani yuboring!")
        return value




class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'year', 'imdb', 'genre', 'actors')




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'movie_id', 'text', 'created_date']
        
    