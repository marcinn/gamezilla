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
	max_players =  models.IntegerField()
	#client = wtf?
	#gameserver = wtf?
    
	def __unicode__(self):
		return self.title

	def get_active_gameplays(self):
		return self.gameplays.filter(status='S')
        
	def get_top_ten(self):
		return self.rankings.order_by ('-score')[:10]

    

STATUS_CHOICES = (
('R', 'Rozpoczęta'),
('O', 'Oczekuje na graczy'),
('Z', 'Zakończona'),
)

class Gameplay(models.Model):
	created_at = models.DateTimeField(default=datetime.datetime.now)
	started_at = models.DateTimeField(null=True, blank=True)
	end_at =  models.DateTimeField(null=True, blank=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	owner = models.ForeignKey(User,  related_name='owned_games')
	player = models.ManyToManyField(User, related_name='playing_game')
	observer = models.ManyToManyField(User, related_name='warching_game')
	game = models.ForeignKey(Game, related_name='gameplays')
	winner = models.ForeignKey(User,  related_name='win_games', null=True, blank=True)

	def __unicode__(self):
		name = self.game.title
		name += " Owner: "+self.owner.username
		name += " Players: "
		for p in self.player.all():
			name+= p.username+" "
		return name

	def start(self):
		self.status = "R"
		self.started_at = datetime.datetime.now()
		self.save()

	def finish(self):
		self.status = "Z"
		self.observer.clear()
		self.end_at = datetime.datetime.now()
		self.save()

	@staticmethod
	def get_by_user (user):
		return Gameplay.objects.filter (player=user).order_by('created_at')

	@staticmethod
	def get_by_user_and_game (user, game):
		return Gameplay.objects.filter (player=user, game=game).order_by('created_at')




class Ranking(models.Model):
	score = models.IntegerField(default=0)
	player = models.ForeignKey(User, related_name='ranging_positions')
	game = models.ForeignKey(Game, related_name='rankings')
	win = models.IntegerField(default=0)
	lost = models.IntegerField(default=0)
	draw = models.IntegerField(default=0)

	def __unicode__ (self):
		return self.player.username + " " +  self.game.title + " " + str(self.score)
		
	@staticmethod
	def get_player_rankig (player, game):
		try:
			return Ranking.objects.get (player=player, game=game)
		except Ranking.DoesNotExist: 
			r = Ranking()
			r.player = player
			r.game = game
			r.save()
			
			return r


	def set_score (self, score):
		self.score = score
		self.save()

	def inc_win (self):
		self.win = win + 1
		self.save()

	def inc_draw (self):
		self.draw = draw + 1
		self.save()
		
	def inc_lost (self):
		self.lost = lost + 1
		self.save()
