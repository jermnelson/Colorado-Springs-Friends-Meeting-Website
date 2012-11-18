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
    url(r"^[newsite/]*accounts/login/$", login),
    url(r"^[newsite/]*accounts/logout/$", logout),
    url(r"^[newsite/]*accounts/profile/$","cosprgssite.Friends.views.display_profile"),
  ##  url(r'^cal/', include('cosprgssite.cal.urls')),
    url(r'^[newsite/]*committees/', include('cosprgssite.committees.urls')),
    url(r'^contact/', "cosprgssite.meetings.views.contact"),
    url(r'^[newsite/]*donate/', include('cosprgssite.donate.urls')),
    url(r'^[newsite/]*email$', 'cosprgssite.views.email', name='email'),
    url(r'^[newsite/]*events/', include('cosprgssite.events.urls')),
    url(r'^[newsite/]*Friends/',include('cosprgssite.Friends.urls')),
    url(r'^[newsite/]*history/', include('cosprgssite.history.urls')),
    url(r'^[newsite/]*meetings/', include('cosprgssite.meetings.urls')),
    url(r'^[newsite/]*reload$', 'cosprgssite.views.reload_rst', name='reload'),
    url(r'^[newsite/]*testimonies/', include('cosprgssite.testimonies.urls')),
    url(r'^[newsite/]*admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^[newsite/]*admin/', include(admin.site.urls)),
)
