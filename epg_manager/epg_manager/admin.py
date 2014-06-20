__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from django.contrib import admin
from epg_core import models

admin.site.register(models.Channel)
admin.site.register(models.Programme)
