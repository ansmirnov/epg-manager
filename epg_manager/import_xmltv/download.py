__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'


import models
from datetime import datetime
import time
from dateutil.parser import parse
from epg_core import models as core_models
import cElementTree as ET
import tempfile
import os
from epg_manager.settings import BASE_DIR


def download_file(url, filename=tempfile.NamedTemporaryFile().name+'.xml'):
    os.system('%s/import_xmltv/download_xmltv.sh "%s" "%s"' % (BASE_DIR, url, filename))
    return filename

class Channel():
    def __init__(self, elem):
        self.elem = elem

    def __getattr__(self, item):
        try:
            if item == 'id':
                return self.elem.get('id')
            if item == 'display_name':
                return self.elem.find('display-name').text
            if item == 'icon':
                return self.elem.find('display-name').get('icon')
        except:
            return ''


class Programme():
    def __init__(self, elem):
        self.elem = elem

    def __getattr__(self, item):
        try:
            if item == 'start':
                return parse(self.elem.get('start'))
            if item == 'stop':
                return parse(self.elem.get('stop'))
            if item == 'duration':
                return self['stop'] - self['start']
            if item == 'channel':
                return self.elem.get('channel')
            if item == 'title':
                return self.elem.find('title').text
            if item == 'category':
                return self.elem.find('category').text
            if item == 'desc':
                return self.elem.find('desc').text
        except:
            return ''


def channels(input_file):
    for event, elem in ET.iterparse(input_file):
        if event == "end" and elem.tag == 'channel':
            yield Channel(elem)


def programmes(input_file):
    for event, elem in ET.iterparse(input_file):
        if event == "end" and elem.tag == 'programme':
            yield Programme(elem)


def download_programmes():
    for afile in models.File.objects.all():
        need_channels = {}
        fn = download_file(afile.filename)
        for channel in models.XMLTVChannel.objects.all().filter(file=afile):
            need_channels[channel.xmltv_id] = channel
            channel.core_channel.clear_programmes()
        for programme in programmes(fn):
            xmltv_id = programme.channel
            if xmltv_id in need_channels.keys():
                core_models.Programme(
                    channel=need_channels[xmltv_id].core_channel,
                    name=programme.title,
                    start=programme.start,
                    stop=programme.stop,
                    description=programme.desc,
                ).save()


def download_programmes():
    for afile in models.File.objects.all():
        need_channels = {}
        fn = download_file(afile.filename)
        for channel in models.XMLTVChannel.objects.all().filter(file=afile):
            need_channels[channel.xmltv_id] = channel
            channel.core_channel.clear_programmes()
        for programme in programmes(fn):
            xmltv_id = programme.channel
            if xmltv_id in need_channels.keys():
                core_models.Programme(
                    channel=need_channels[xmltv_id].core_channel,
                    name=programme.title,
                    start=programme.start,
                    stop=programme.stop,
                    description=programme.desc,
                ).save()
        os.remove(fn)

        os.remove(fn)
