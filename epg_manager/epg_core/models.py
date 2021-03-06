from django.db import models
import datetime


class Stream(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
	return self.name


class Channel(models.Model):
    name = models.CharField(max_length=250)
    stream = models.ForeignKey(Stream)

    def __unicode__(self):
        return self.name

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

    def str_description(self):
	return self.description.replace('\n', '')

    def __unicode__(self):
        return self.channel.name + ' - ' + self.name

