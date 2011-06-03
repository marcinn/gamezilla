from django.conf.urls.defaults import *


urlpatterns = patterns('game.views',
    # Example:
    # (r'^zillaportal/', include('zillaportal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^$', 'gamelist'),
    (r'^active/$', 'gameplays'),
    (r'^active/(?P<sort>\w{1,20})$', 'gameplays'),
	(r'^active/create/(?P<game_id>\d{1,10})$', 'create_game'),
	(r'^active/start/(?P<game_id>\d{1,10})$', 'start_game'),
    (r'^active/join/(?P<game_id>\d{1,10})$', 'join_game'),
    (r'^active/watch/(?P<game_id>\d{1,10})$', 'watch_game'),
	(r'^active/leave/(?P<game_id>\d{1,10})$', 'leave_game'),
    (r'^details/(?P<game_id>\d{1,10})$', 'game_detail'),
    (r'^user/(?P<username>\w{1,20})/game/(?P<game_id>\d{1,10})$', 'user_gameplays'),
)

