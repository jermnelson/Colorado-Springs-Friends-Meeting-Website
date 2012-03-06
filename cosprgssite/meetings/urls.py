"""
 mod:`url` Quaker Meetings URL routing
"""
__author__ = 'Jeremy Nelson'
import meetings.views
from django.conf.urls.defaults import *

urlpatterns = patterns('meetings.views',
    url(r"^$","default",name='Meetings Home'),
    url(r"[a|A]dvices[a|A]nd[q|Q]ueries","advices_and_queries"),
    url(r'[b|B]usiness$','business'),
    url(r'[s|S]pecial$','special'),
    url(r'[w|W]orship$','worship'),
)
