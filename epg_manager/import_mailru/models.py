from django.db import models
from epg_core import models as core_models
from datetime import datetime, date
from time import sleep
import urllib3
import json
from clean_html import clean

class MailRuChannel(models.Model):
    core_channel = models.ForeignKey(core_models.Channel)
    mailru_id = models.IntegerField()

    def update(self):
        self.core_channel.clear_programmes()
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://tv.mail.ru/ext/admtv/?sch.main=1&sch.channel=%d' % self.mailru_id)
        days = json.loads(r.data)['state']['days']
        for day in days:
            curday = datetime.strptime(day, '%Y-%m-%d')
            if curday.date() < date.today():
                continue
            r = http.request('GET', 'http://tv.mail.ru/ext/admtv/?sch.main=1&sch.channel=%d&sch.date=%s' % (self.mailru_id, day))
            data = json.loads(r.data)
            for programme in data['channel_type'].values()[0][0]['schedule']:
                rdescr = http.request('GET', 'http://tv.mail.ru/ext/admtv/?sch.tv_event_id=%s&sch.channel_region_id=147' % (programme['id']))
                descr = clean(json.loads(rdescr.data)['tv_event']['descr'])
                core_models.Programme(
                    channel=self.core_channel,
                    name=programme['name'],
                    start=datetime.strptime(programme['start'], '%Y-%m-%d %H:%M:%S'),
                    stop=datetime.strptime(programme['stop'], '%Y-%m-%d %H:%M:%S'),
                    description=descr,
                ).save()
                sleep(2)
#                break
