from django.db import models
from epg_core import models as core_models

class File(models.Model):
    name = models.CharField(max_length=100)
    filename = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.filename)

class XMLTVChannel(models.Model):
    core_channel = models.ForeignKey(core_models.Channel)
    xmltv_id = models.CharField(max_length=150)
    file = models.ForeignKey('File')

    def __unicode__(self):
        return "%s %s" % (self.xmltv_id, self.core_channel.name)

