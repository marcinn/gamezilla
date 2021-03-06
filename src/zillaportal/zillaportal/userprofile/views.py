import urlparse

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.sites.models import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from models import Friendlist


import forms


@csrf_protect
@never_cache
def login(request, template_name='profile/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):

    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = authentication_form(data=request.POST)
        if form.is_valid():
            netloc = urlparse.urlparse(redirect_to)[1]

            if not redirect_to:
                redirect_to = '/index'


            elif netloc and netloc != request.get_host():
                redirect_to = settings.LOGIN_REDIRECT_URL

            auth_login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)
        
    request.session.set_test_cookie()

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    context.update(extra_context or {})
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request, current_app=current_app))
                              
@login_required
def base (request):
	
	f = None
	if request.method=="POST":
		f = forms.UploadAvatar (request.POST, request.FILES)
	else:
		f = forms.UploadAvatar ()
		
	return render_to_response('profile/base.html', {'uploadavatar' : f}, context_instance=RequestContext(request))


def logout_view (request):
	logout(request)
	
	return HttpResponseRedirect('/')
	
def register(request):
	success = False
	if request.method == "POST":
		form = forms.RegisterForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			success = True
			
			user.backend = 'django.contrib.auth.backends.ModelBackend'
			auth_login(request, user)
			
			return HttpResponseRedirect('/index')
                  
	else:
		#form = forms.RegisterForm(user=request.user)
		form = forms.RegisterForm()
    
 	context = {'form': form, 'success' : success} 	
 	
	return render_to_response('profile/register.html', context, context_instance=RequestContext(request))

@login_required
def userprofile (request, id=None, name=None):
	
	
	
	user = None
	if id is not None and name is None:
		user = get_object_or_404 (User, pk=id)
	elif id is None and name is not None:
		user = get_object_or_404 (User, username=name)

	if request.user == user:
		return base (request)
	
 	context = {'userprofile': user}
 	
 	uprofile = request.user.get_profile()
 	lol = uprofile.count_firends()
	context['friend_status'] = uprofile.is_friend(user)

	return render_to_response('profile/userprofile.html', context, context_instance=RequestContext(request))

@login_required
def invite (request, id=None, name=None):
	
	user = None
	if id is not None and name is None:
		user = get_object_or_404 (User, pk=id)
	elif id is None and name is not None:
		user = get_object_or_404 (User, username=name)
		
	request.user.get_profile().invite_friend(user)
	
	return userprofile (request, id, name)


@login_required
def invitation (request, id=None, action=None):
	
	inv= get_object_or_404 (Friendlist, pk=id)
	
	if inv.invited == request.user:
		if action == 'accept':
			inv.accept()
		elif action == 'decline':
			inv.decline()
		elif action == 'delete':
			inv.delete_friendship()	
	
	return base (request)
