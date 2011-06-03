# -*- coding: utf-8 -*

import urlparse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Game, Gameplay
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime  


from django.shortcuts import get_object_or_404

def index(request):

    return render_to_response('index.html', context_instance=RequestContext(request))

    
def gamelist(request):
	games = Game.objects.order_by('title')
	
	return render_to_response('game/gamelist.html', {'games' : games}, context_instance=RequestContext(request))


def gameplays(request, sort='status'):
	sort='-' + sort
	print sort
	list_games = Gameplay.objects.filter(~Q(status='Z')).order_by(sort)
	
	return render_to_response('game/list.html', {'list' : list_games}, context_instance=RequestContext(request))
	
def user_gameplays (request, username, game_id):
	
	 user = get_object_or_404 (User, username=username)
	 game = get_object_or_404 (Game, pk=game_id)
	 
	 list_games = Gameplay.get_by_user_and_game (user, game)
	 
	 return render_to_response('game/user_gameplays.html', {'list' : list_games, 'player': user, 'game': game}, context_instance=RequestContext(request))

def create_game(request, game_id):
	new = get_object_or_404(Game, id=game_id)
	new_game = Gameplay(game=new, owner = request.user, status='O')
	new_game.save()
	new_game.player.add(request.user)
	
	return gameplays(request)
	
def start_game(request, game_id):
	game = get_object_or_404(Gameplay, id=game_id)
	if request.user == game.owner:
		game.status = 'R'
		game.started_at = datetime.now()
		game.save()
	
	return gameplays(request)
	
def join_game(request, game_id):
	
	gameplay = get_object_or_404(Gameplay, id=game_id)
	if request.user not in game.player and equest.user not in game.observer:
		if gameplay.game.max_players > game.player.count():
			game.player.add(request.user)
		
	return gameplays(request)
	
def watch_game (request, game_id):
	
	gameplay = get_object_or_404(Gameplay, id=game_id)
	if request.user not in game.player and equest.user not in game.observer:
		if gameplay.status != "F":
			gameplay.observer.add(request.user)
		
	return gameplays(request)
	
def leave_game(request, game_id):
	game = get_object_or_404(Gameplay, id=game_id)
	game.player.remove(request.user)
	game.observer.remove(request.user)
		
	return gameplays(request)
	
	

def game_detail (request, game_id):
	
	game = get_object_or_404 (Game, id=game_id)
	
	return render_to_response('game/detail.html', {'game' : game}, context_instance=RequestContext(request))

