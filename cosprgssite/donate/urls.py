"""
 mod:`url` Quaker Donation URL routing
"""
__author__ = 'Jeremy Nelson'
import donate.views
from django.conf.urls.defaults import *

urlpatterns = patterns('donate.views',
    url(r"^$","default"),
)
