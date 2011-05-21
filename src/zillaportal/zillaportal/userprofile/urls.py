from django.conf.urls.defaults import *


urlpatterns = patterns('',
    # Example:
    # (r'^zillaportal/', include('zillaportal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^$', 'userprofile.views.base'),
    (r'^logout/$', 'userprofile.views.logout_view'),
)

