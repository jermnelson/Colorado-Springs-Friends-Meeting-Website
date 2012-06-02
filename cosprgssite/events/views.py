__author__ = "Jeremy Nelson"

import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.generic.simple import direct_to_template
from models import MeetingEvent

def default(request):
    today = datetime.datetime.today()
    first_day = datetime.datetime(today.year,today.month,1)
    events = MeetingEvent.objects.filter(start_on__gte=first_day)
    return direct_to_template(request,
                              'events/index.html',
                              {'current':today,
                               'events':events})

def day_display(request,
                year,
                month,
                day):
    current = datetime.datetime(int(year),int(month),int(day))
    meeting_events = MeetingEvent.objects.filter(
                           start_on__year=current.year
                       ).filter(
                           start_on__month=current.month
                       ).filter(
                           start_on__day=current.day)
    return direct_to_template(request,
                              'events/day.html',
                              {'current':current,
                               'meeting_events':meeting_events})

def month_display(request,
                  year,
                  month):
    month_start = datetime.datetime(int(year),int(month),1)
    meeting_events = MeetingEvent.objects.filter(start_on__gte=month_start)
    return direct_to_template(request,
                              'events/month.html',
                              {'current':month_start,
                               'meeting_events':meeting_events})
                           
    
