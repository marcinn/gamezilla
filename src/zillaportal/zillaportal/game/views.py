# -*- coding: utf-8 -*

import urlparse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Game, Gameplay
from django.contrib.auth.models import User


def index(request):

    return render_to_response('index.html', context_instance=RequestContext(request))

    
def gamelist(request):
	games = Game.objects.order_by('title')
	
	return render_to_response('game.html', {'games' : games}, context_instance=RequestContext(request))


def gameplays(request):
	list_games = Gameplay.objects.order_by('created_at')
	
	try:
		player = list_games.objects.get (username = request.user.username)
	except User.DoesNotExist:
		player = False
	
	
	
	return render_to_response('game/list.html', {'list' : list_games, 'player' : player}, context_instance=RequestContext(request))

def create_game(request):
	games = Game.objects
	
def join_game(request, id):
	game = Gameplay.objects.get(pk=id)
	game.player.add(request.user)
		
	return render_to_response('game/join.html', context_instance=RequestContext(request))
	
def leave_game(request, id):
	game = Gameplay.objects.get(pk=id)
	game.player.remove(request.user)
		
	return render_to_response('game/leave.html', context_instance=RequestContext(request))
	
	

