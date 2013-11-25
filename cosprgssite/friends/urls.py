__author__ = "Jeremy Nelson"

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'friends.views.default'),
    (r'^update$', 'friends.views.update'),
    (r'^pw$', 'friends.views.update_pw'),
    (r'^(?P<username>.*)$', 'friends.views.friend'),
                       
)
