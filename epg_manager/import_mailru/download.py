__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'


import models

def download_programmes():
    for channel in models.MailRuChannel.objects.all():
        channel.update()