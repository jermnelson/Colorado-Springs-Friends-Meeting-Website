"""
 :mod:`views` 
"""
__author__ = 'Jeremy Nelson'

import datetime
from django.contrib.auth import authenticate
from django.views.generic.simple import direct_to_template
from meetings.models import MeetingEvent

class Events(object):

    def __init__(self,**kwargs):
        self.events = []
        if 'meeting' in kwargs:
            self.events.append(kwargs.get('meeting'))

    def day_url(self,year,month,day,has_event=False):
        return ''

    def month_url(self,year,month):
        return ''

    def events_by_day(self,year,month):
        return dict()
                               

def home(request):
    """
    Default view for Colorado Springs Monthly Meeting Website
    """
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    event_query = MeetingEvent.objects.all()
    events = Events()
    return direct_to_template(request,
                              'index.html',
                             {'events':events,
                              'user':user})
