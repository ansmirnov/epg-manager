# -*- coding: iso-8859-1 -*-

import sys, os
import django.core.handlers.wsgi

sys.path.insert(0, '/var/www/epg-manager/epg_manager/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'epg_manager.settings'

application = django.core.handlers.wsgi.WSGIHandler()
