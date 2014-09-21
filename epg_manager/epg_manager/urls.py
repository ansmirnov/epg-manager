from django.conf.urls import patterns, include, url
import export_csv.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'epg_manager.views.home', name='home'),
    url(r'^export_csv/', include('export_csv.urls')),
    url(r'^export_print/', include('export_print.urls')),
    url(r'^luminato/', include('luminato.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
