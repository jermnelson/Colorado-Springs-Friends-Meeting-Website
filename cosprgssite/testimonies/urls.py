"""
 mod:`url` Quaker Testimonies URL routing
"""
__author__ = 'Jeremy Nelson'
import testimonies.views
from django.conf.urls.defaults import *

urlpatterns = patterns('testimonies.views',
    url(r"^$","default",name='Testimonies Home'),
    url(r'[c|C]ommunity$','community'),
    url(r'[e|E]quality$','equality'),
    url(r'[i|I]ntegrity$','integrity'),
    url(r'peace$','peace'),
    url(r'[s|S]implicity$','simplicity'),
    url(r'[t|T]ruth$','truth'),
)
