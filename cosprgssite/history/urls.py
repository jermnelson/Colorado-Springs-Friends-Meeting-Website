"""
 mod:`url` Quaker History URL routing
"""
__author__ = 'Jeremy Nelson'
import history.views
from django.conf.urls.defaults import *

urlpatterns = patterns('history.views',
    url(r"^$","default",name='History Home'),
    url(r'[o|O]rigin$','george_fox_first_quakers'),
    url(r'[r|R]eligious[s|S]ociety[o|O]f[f|F]riends$','religious_society_of_friends'),
    url(r'[h|H]icksite$','hicksite'),
    url(r'[a|A]bolition[a|A]nd[s|S]uffrage$','abolition_and_suffrage'),
    url(r'[c|C]olorado[s|S]prings$','colorado_springs'),
    url(r'[w|W]orldWars[a|A]nd[c|C]onscientious[o|O]bjectors$',"worldwars_conscientious_objectors"),
)
