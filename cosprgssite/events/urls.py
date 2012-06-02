"""
 mod:`url` Quaker events URL routing
"""
__author__ = 'Jeremy Nelson'
import events.views
from django.conf.urls.defaults import *

urlpatterns = patterns('events.views',
    url(r"^$","default",name='Events Home'),
    url(r"(\d{4})/(\d{2})/$","month_display"),
    url(r"(\d{4})/(\d{2})/(\d{2})/$","day_display"),
)
