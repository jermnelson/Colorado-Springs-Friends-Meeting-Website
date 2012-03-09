"""
 mod:`url` Quaker Committee URL routing
"""
__author__ = 'Jeremy Nelson'
import views
from django.conf.urls.defaults import *

##urlpatterns = patterns('',
##   (r'(\d{4})/(\d{2})/$','get_report'),
##)

urlpatterns = patterns('committees.views',
    url(r"^$","default",name='Committee Home'),
    url(r"^save$","save_committee"),
    url(r"(?P<committee>\w+)/members/add$","add_member"),
    url(r"(?P<committee>\w+)/reports/add$","add_report"),
    url(r'^(?P<committee>\w+)/(?P<year>\d+)/(?P<month>\w+)/(?P<report_name>\w+)/$','display_monthly_report'),
    url(r"(?P<committee>\w+)/$","display_committee"),
    ## url(r"^(\w+)/(\d+)/$","display_yearly_report")
)
