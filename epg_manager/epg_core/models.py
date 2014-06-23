from django.db import models
import datetime


class Channel(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

    def update(self):
        for channel in self.mailruchannel_set.all():
            channel.update()

    def clear_programmes(self):
        self.programme_set.all().delete()


class Programme(models.Model):
    channel = models.ForeignKey('Channel')
    name = models.CharField(max_length=250)
    description = models.TextField()
    start = models.DateTimeField()
    stop = models.DateTimeField()

    def duration(self):
        return self.stop - self.start

    def __unicode__(self):
        return self.channel.name + ' - ' + self.name

