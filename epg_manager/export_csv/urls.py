from django.conf.urls import patterns, include, url
from export_csv.views import *


urlpatterns = patterns('',
    url(r'^', export_csv),
)