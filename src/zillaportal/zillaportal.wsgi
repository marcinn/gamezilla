import os
import sys

path = '/path/to/mysite'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'zillaportal.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
