from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    games_played = models.IntegerField()
    avatar_image = models.ImageField(upload_to='images')
    level =  models.IntegerField()
    about = models.CharField(max_length=500)

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    screenshot = models.ImageField(upload_to='images')
    games_count = models.IntegerField()
    #client = wtf?
    #gameserver = wtf?

class Gameplay(models.Model):
    created_at = models.DateTimeField()
    started_at = models.DateTimeField()
    end_at =  models.DateTimeField()
    status = models.CharField(max_length=1)
    owner = models.ForeignKey(User,  related_name='owned_games')
    player = models.ManyToManyField(User, related_name='playing_game')
    game = models.ForeignKey(Game)


class Ranking(models.Model):
    score = models.IntegerField()