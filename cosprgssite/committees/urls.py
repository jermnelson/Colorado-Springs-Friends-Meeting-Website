"""
 mod:`url` Quaker Committee URL routing
"""
__author__ = 'Jeremy Nelson'
import testimonies.views
from django.conf.urls.defaults import *

urlpatterns = patterns('committees.views',
    url(r"^$","default",name='Committee Home'),
    url(r'^/(\d{4})/(\d{2}/{\d{2}/$','get_report'),
##    url(r'equality$','equality'),
##    url(r'integrity$','integrity'),
##    url(r'peace$','peace'),
##    url(r'simplicity$','simplicity'),
##    url(r'truth$','truth'),
)
