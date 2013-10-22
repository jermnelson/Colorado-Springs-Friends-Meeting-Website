__author__ = "Jeremy Nelson"

from collections import OrderedDict
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from meetings import get_minute, get_minutes, QUAKER_MONTHS

def home(request):
    return render(request,
                  'index.html',
                  {'category': 'home'})


def meeting(request,
            meeting=None):
    if meeting:
        if meeting == 'Business':
            minutes = OrderedDict()
            all_minutes = get_minutes()
            for i,row in enumerate(all_minutes):
                if i > 0 or i <= len(all_minutes):
                    current_year = row.get('date').year
                    if current_year == all_minutes[i-1].get('date').year:
                        minutes[current_year].append(row)
                    else:
                        minutes[current_year] = [row,]
            print(minutes[2011])
            return render(request,
                          'business.html',
                          {'category': 'about',
                           'minutes': minutes,
                           'section': 'meeting'})
                          
        return render(request,
                      '{0}.html'.format(meeting.lower()),
                      {'category': 'about',
                       'section': 'meeting'})
    else:
        return render(request,
                      'meetings.html',
                      {'category': 'about',
                       'section': 'meeting'})

def minute(request,
           meeting=None,
           year=None,
           month=None):
    if meeting:
        if meeting == 'Business':
            minute_html = get_minute(year,
                                     month)
            return render(request,
                          'minute.html',
                          {'category': 'about',
                           'content': minute_html,
                           'section': 'meeting'})
        
def testimony(request,
              testimony=None):
    if testimony:
        return render(request,
                      '{0}.html'.format(testimony.lower()),
                      {'category':'about',
                       'section': 'testimonies'})
    else:
        return render(request,
                      'testimonies.html',
                      {'category':'about',
                       'section': 'testimonies'})
    
