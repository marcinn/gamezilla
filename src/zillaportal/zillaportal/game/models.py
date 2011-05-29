# -*- coding: utf-8 -*

from django.db import models

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import datetime



class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    screenshot = models.ImageField(upload_to='images/games', null=True, blank=True)
    games_count = models.IntegerField()
    #client = wtf?
    #gameserver = wtf?
    
    def __unicode__(self):
        return self.title

    def get_active_gameplays(self):
        return self.gameplays.filter(status='S')

    

STATUS_CHOICES = (
('S', 'Started'),
('W', 'Waiting for players'),
('F', 'Game finished'),
)

class Gameplay(models.Model):
    created_at = models.DateTimeField()
    started_at = models.DateTimeField()
    end_at =  models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    owner = models.ForeignKey(User,  related_name='owned_games')
    player = models.ManyToManyField(User, related_name='playing_game')
    game = models.ForeignKey(Game, related_name='gameplays')

    def __unicode__(self):
        name = self.game.title
        name += " Owner: "+self.owner.username
        name += " Players: "
        for p in self.player.all():
            name+= p.username+" "
        return name

    def start(self):
        self.status = "S"
        self.started_at = datetime.datetime.now()
        self.save()

    def finish(self):
        self.status = "F"
        self.end_at = datetime.datetime.now()
        self.save()




class Ranking(models.Model):
    score = models.IntegerField()

