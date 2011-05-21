from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^zillaportal/', include('zillaportal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^$', 'game.views.index'),
    (r'^index/$', 'game.views.index'),

    (r'^game/', include('game.urls')),

    (r'^profile/', include('userprofile.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
