"""
 mod:`url` Quaker events URL routing
"""
__author__ = 'Jeremy Nelson'
import events.views
from django.conf.urls.defaults import *

urlpatterns = patterns('events.views',
    url(r"^$","default",name='Events Home')
)
