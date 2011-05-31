from django.conf.urls.defaults import *


urlpatterns = patterns('game.views',
    # Example:
    # (r'^zillaportal/', include('zillaportal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^$', 'gamelist'),
    (r'^active/$', 'gameplays')
)

