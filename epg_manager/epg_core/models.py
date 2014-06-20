from django.db import models
import datetime


class Channel(models.model):
    name = models.CharField(max_length=250)


class Programme(models.model):
    channel = models.ForeignKey('Channel')
    name = models.CharField(max_length=250)
    description = models.TextField()
    start = models.DateTimeField()
    stop = models.DateTimeField()

