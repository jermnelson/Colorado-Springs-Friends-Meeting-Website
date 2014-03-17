__author__ = "Jeremy Nelson"

import json
import logging
import os
import sys

from collections import OrderedDict
import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from committees import get_report, get_reports
from friends.models import Committee, CommitteeMembership
from meetings import get_minute, get_minutes, QUAKER_MONTHS


def calendar(request):
    return render(request,
                  'calendar.html',
                  {'category': 'calendar',
                   'section': 'calendar'})

def committee(request,
              committee):
    committee_ = Committee.objects.all().get(name=committee)
    committee_membership = CommitteeMembership.objects.all().filter(
        committee=committee_)
    committee_membership = sorted(committee_membership,
                                  key=lambda x: x.friend.user.last_name)
    if not request.user.is_authenticated() and committee == 'MinistryAndOversight':
        reports = []
    else:
        reports = sorted(get_reports(committee))
    return render(request,
                  '{0}.html'.format(committee.lower()),
                  {'category': 'about',
                   'Committee': committee,
                   'section': 'committee',
                   'membership': committee_membership,
                   'reports': reports})

def history(request,
            topic):
    return render(request,
                  '{0}.html'.format(topic),
                  {'category': 'about',
                   'section': 'history'})
                   

def home(request):
    return render(request,
                  'index.html',
                  {'category': 'home'})

def json_view(func):
    """
    Returns JSON results from method call, from Django snippets
    `http://djangosnippets.org/snippets/622/`_
    """
    def wrap(request, *a, **kw):
        response = None
        try:
            func_val = func(request, *a, **kw)
            assert isinstance(func_val, dict)
            response = dict(func_val)
            if 'result' not in response:
                response['result'] = 'ok'
        except KeyboardInterrupt:
            raise
        except Exception,e:
            exc_info = sys.exc_info()
            print(exc_info)
            logging.error(exc_info)
            if hasattr(e,'message'):
                msg = e.message
            else:
                msg = ugettext("Internal error: %s" % str(e))
            response = {'result': 'error',
                        'text': msg}
        json_output = json.dumps(response)
        return HttpResponse(json_output,
                            mimetype='application/json')
    return wrap

def login_view(request):
    user = authenticate(username=request.POST.get('username'),
                        password=request.POST.get('password'))
    if user is None:
        messages.error(request, "Username and/or Password invalid")
    else:
        login(request, user)
    return redirect("/")


def logout_view(request):
    current_path = request.POST.get('current', "/")
    logout(request)
    return redirect(current_path)

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
        
def report(request,
           committee,
           year,
           month):
    if not request.user.is_authenticated() and committee == 'MinistryAndOversight':
        raise Http404
    report_html = get_report(year,
                             month,
                             committee,)
    if report_html is not None:
        return render(request,
                      'report.html',
                      {'category': 'about',
                       'content': report_html,
                       'section': 'committee'})
    else:
        raise Http404
    

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
    
