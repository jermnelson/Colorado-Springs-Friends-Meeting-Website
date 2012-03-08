from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cosprgssite.views.home', name='home'),
    url(r'^committees/', include('cosprgssite.committees.urls')),
    url(r'^Friends/',include('cosprgssite.Friends.urls')),
    url(r'^history/', include('cosprgssite.history.urls')),
    url(r'^meetings/', include('cosprgssite.meetings.urls')),
    url(r'^testimonies/', include('cosprgssite.testimonies.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
