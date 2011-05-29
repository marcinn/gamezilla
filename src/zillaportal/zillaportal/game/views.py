# -*- coding: utf-8 -*

import urlparse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Game


def index(request):

    return render_to_response('index.html', context_instance=RequestContext(request))

    
def gamelist(request):
	games = Game.objects.order_by('title')
	
	return render_to_response('game.html', {'games' : games}, context_instance=RequestContext(request))

