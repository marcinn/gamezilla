from django.conf.urls.defaults import *


urlpatterns = patterns('game.views',
    # Example:
    # (r'^zillaportal/', include('zillaportal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^$', 'gamelist'),
    (r'^active/$', 'gameplays'),
    (r'^active/join/(?P<id>\d{1,10})$', 'join_game'),
	(r'^active/leave/(?P<id>\d{1,10})$', 'leave_game'),
)

