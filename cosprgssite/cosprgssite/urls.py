__author__ = "Jeremy Nelson"

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^meetings/(?P<meeting>.*)/(?P<year>\d+)/(?P<month>\d+)$',
        'cosprgssite.views.minute',
        name='minute'),
    url(r'^meetings/(?P<meeting>.*)$',
        'cosprgssite.views.meeting',
        name='meeting'),
    url(r'^testimonies/(?P<testimony>.*)$',
        'cosprgssite.views.testimony',
        name='testimony'),
    url(r'^$', 'cosprgssite.views.home', name='home'),
                       
    # url(r'^cosprgssite/', include('cosprgssite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
