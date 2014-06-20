__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from django.contrib import admin
from import_mailru import models

admin.site.register(models.MailRuChannel)
