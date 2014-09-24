from django.conf.urls import patterns, include, url
from export_csv.views import *


urlpatterns = patterns('',
    url(r'^(\d+)', export_csv_stream),
    url(r'^', export_csv),
)
