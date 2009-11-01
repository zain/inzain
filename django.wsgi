import os
import sys
import site

# virtualenv
site.addsitedir('/usr/local/pythonenv/blog/lib/python2.6/site-packages')

sys.path.append('/var/www/inzain.net/blog/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'inzain.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
