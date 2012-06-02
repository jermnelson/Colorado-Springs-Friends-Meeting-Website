"""
 :mod:`urls` Colorado Springs Friends Meeting site URLS
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'cosprgssite.views.home', name='home'),
    url(r"^accounts/login/$", login),
    url(r"^accounts/logout/$", logout),
    url(r"^accounts/profile/$","cosprgssite.Friends.views.display_profile"),
  ##  url(r'^cal/', include('cosprgssite.cal.urls')),
    url(r'^committees/', include('cosprgssite.committees.urls')),
    url(r'^contact/', "cosprgssite.meetings.views.contact"),
    url(r'^donate/', include('cosprgssite.donate.urls')),
    url(r'^events/', include('cosprgssite.events.urls')),
    url(r'^Friends/',include('cosprgssite.Friends.urls')),
    url(r'^history/', include('cosprgssite.history.urls')),
    url(r'^meetings/', include('cosprgssite.meetings.urls')),
    url(r'^testimonies/', include('cosprgssite.testimonies.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
