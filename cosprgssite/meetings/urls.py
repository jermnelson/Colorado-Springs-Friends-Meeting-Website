"""
 mod:`url` Quaker Meetings URL routing
"""
__author__ = 'Jeremy Nelson'
import meetings.views
from django.conf.urls.defaults import *

urlpatterns = patterns('meetings.views',
    url(r"^$","default",name='Meetings Home'),
    url(r'[b|B]usiness$','business'),
    url(r'[s|S]pecial$','special'),
    url(r'[w|W]orship$','worship'),
)
