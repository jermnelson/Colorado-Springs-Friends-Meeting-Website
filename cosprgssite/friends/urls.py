__author__ = "Jeremy Nelson"

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^(?P<username>.*)$', 'friends.views.friend'))
