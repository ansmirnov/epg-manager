from django.conf.urls import patterns, include, url
from export_print.views import *


urlpatterns = patterns('',
    url(r'^', export_print),
)
