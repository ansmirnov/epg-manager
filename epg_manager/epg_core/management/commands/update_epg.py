__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from epg_core import models
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = 'Update statuses for all users'

    def handle_noargs(self, **options):
        for channel in models.Channel.objects.all():
            channel.update()