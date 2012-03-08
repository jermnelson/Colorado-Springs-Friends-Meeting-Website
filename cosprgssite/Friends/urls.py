"""
 mod:`url` Quaker URL routing
"""
__author__ = 'Jeremy Nelson'
import Friends.views
from django.conf.urls.defaults import *

##urlpatterns = patterns('',
##   (r'(\d{4})/(\d{2})/$','get_report'),
##)

urlpatterns = patterns('Friends.views',
    url(r"^$","default"),
    url(r"(?P<username>\w+)/$","display_friend"),
)
