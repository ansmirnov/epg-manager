from django.db import models
from epg_core import models as core_models


class MailRuChannel(models.Model):
    core_channel = models.ForeignKey(core_models.Channel)
    mailru_id = models.IntegerField()
