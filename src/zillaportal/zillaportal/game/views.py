# -*- coding: utf-8 -*

import urlparse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Game, Gameplay


def index(request):

    return render_to_response('index.html', context_instance=RequestContext(request))

    
def gamelist(request):
	games = Game.objects.order_by('title')
	
	return render_to_response('game.html', {'games' : games}, context_instance=RequestContext(request))


def gameplays(request):
	list_games = Gameplay.objects.order_by('created_at')
	
	return render_to_response('game/list.html', {'list' : list_games}, context_instance=RequestContext(request))

def create_game(request):
	games = Game.objects
	
