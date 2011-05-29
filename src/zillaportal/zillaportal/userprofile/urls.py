from django.conf.urls.defaults import *


urlpatterns = patterns('userprofile.views',
    # Example:
    # (r'^zillaportal/', include('zillaportal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^$', 'base'),
    (r'^login/$', 'login'),
    (r'^logout/$', 'logout_view'),
    (r'^register/$', 'register'),
    (r'^user/(?P<id>\d{1,10})$', 'userprofile'),
    (r'^user/(?P<name>\w{1,20})$', 'userprofile'),
    (r'^invite/(?P<name>\w{1,20})$', 'invite'),
    (r'^invitation/(?P<id>\d{1,10})/(?P<action>\w{1,10})$', 'invitation'),
)

