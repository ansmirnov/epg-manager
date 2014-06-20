from django.db import models
import datetime


class Channel(models.Model):
    name = models.CharField(max_length=250)


class Programme(models.Model):
    channel = models.ForeignKey('Channel')
    name = models.CharField(max_length=250)
    description = models.TextField()
    start = models.DateTimeField()
    stop = models.DateTimeField()

