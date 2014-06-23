__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from django.contrib import admin
from epg_core import models

class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('name', 'channel', 'start', 'stop')

admin.site.register(models.Channel)
admin.site.register(models.Programme, ProgrammeAdmin)
