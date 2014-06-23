__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from epg_manager import settings
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = 'Update statuses for all users'

    def handle_noargs(self, **options):
        import_apps = [x for x in settings.INSTALLED_APPS if x.find('import_') == 0]
        for app in import_apps:
            mod = __import__(app+'.download')
            mod.download.download_programmes()
