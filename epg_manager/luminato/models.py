from django.db import models
from epg_core.models import Channel


class LuminatoChannel(models.Model):
    channel = models.OneToOneField(Channel)
    tsid = models.CharField(max_length=50, verbose_name="Transport Stream ID")
    sid = models.CharField(max_length=50, verbose_name="SID")
    #oid = models.CharField(max_length=50, verbose_name="Original Network ID")

    def __unicode__(self):
        return "%s tsid:%s sid:%s" % (self.channel.__unicode__(), self.tsid, self.sid)

    def english_name(self):
        return 'tv_%d' % self.channel.pk
