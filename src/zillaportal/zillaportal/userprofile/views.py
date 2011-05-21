from django.template import RequestContext
from django.shortcuts import render_to_response

def base (request):
	
	
    return render_to_response('profile/base.html', context_instance=RequestContext(request))


def logout_view (request):
	
	
	 return render_to_response('profile/base.html', context_instance=RequestContext(request))
