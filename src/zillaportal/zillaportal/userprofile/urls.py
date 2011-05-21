from django.conf.urls.defaults import *


urlpatterns = patterns('userprofile.views',
    # Example:
    # (r'^zillaportal/', include('zillaportal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^$', 'base'),
    (r'^login/$', 'login'),
    (r'^logout/$', 'logout_view'),
)

