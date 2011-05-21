import urlparse

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.sites.models import get_current_site


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
                              

def base (request):
	
	
    return render_to_response('profile/base.html', context_instance=RequestContext(request))


def logout_view (request):
	logout(request)
	
	return HttpResponseRedirect('/')
	
def register(request):
	success = False
	if request.method == "POST":
		form = registration_form(data=request.POST)
		if form.is_valid():
            form.save()
            success = True
                  
	else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
        'success' : success,
    }
	return render_to_response('profile/register.html', context, context_instance=RequestContext(request))
