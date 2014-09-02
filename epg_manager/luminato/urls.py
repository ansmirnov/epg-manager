from django.conf.urls import patterns, include, url
from luminato.views import config


urlpatterns = patterns('',
    url(r'^', config),
)
