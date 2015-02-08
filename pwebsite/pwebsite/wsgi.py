import os
import sys
import site

PROJECT_ROOT = '/srv/www/royrvik.org/new-website/pwebsite/'
site_packages = os.path.join(PROJECT_ROOT, '../env/lib/python2.7/site-packages')
site.addsitedir(os.path.abspath(site_packages))
sys.path.insert(0, site_packages)
sys.path.insert(0, PROJECT_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'pwebsite.settings'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
