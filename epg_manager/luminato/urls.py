from django.conf.urls import patterns, include, url
from luminato.views import config, config_stream


urlpatterns = patterns('',
    url(r'^(\d+)', config_stream),
    url(r'^', config),
)
