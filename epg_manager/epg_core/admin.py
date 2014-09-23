__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from django.contrib import admin
from epg_core import models

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('name', 'channel', 'start', 'stop')

admin.site.register(models.Channel, ChannelAdmin)
admin.site.register(models.Programme, ProgrammeAdmin)
admin.site.register(models.Stream)
