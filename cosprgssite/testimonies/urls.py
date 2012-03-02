"""
 mod:`url` Quaker Testimonies URL routing
"""
__author__ = 'Jeremy Nelson'
import testimonies.views
from django.conf.urls.defaults import *

urlpatterns = patterns('testimonies.views',
    url(r"^$","default",name='Testimonies Home'),
    url(r'community$','community'),
    url(r'equality$','equality'),
    url(r'integrity$','integrity'),
    url(r'peace$','peace'),
    url(r'simplicity$','simplicity'),
    url(r'truth$','truth'),
)
