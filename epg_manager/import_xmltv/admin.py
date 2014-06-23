__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from django.contrib import admin
from import_xmltv import models

admin.site.register(models.XMLTVChannel)
admin.site.register(models.File)
