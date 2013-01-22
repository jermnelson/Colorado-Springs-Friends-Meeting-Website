"""
  :mod:`views` Views for Meetings 
"""
__author__ = 'Jeremy Nelson'
import logging
from datetime import datetime
from django.contrib.auth import authenticate
from django.core.cache import cache
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from meetings.forms import MeetingReportForm
from meetings.models import MEETING_TYPES, REPORT_TYPES, MeetingReport, QUAKER_MONTHS
#from committees.views import get_report
from django_helpers import get_year
from django.contrib.auth.models import User
from quakers.forms import EmailContactForm

MEETING_TYPES_DICT = {}
for row in MEETING_TYPES:
    MEETING_TYPES_DICT[row[1]] = row[0]


ARCHIVE_YEARS = [2011,2012]

def default(request):
    """
    Default view for Meetings
    """
    business_minutes = MeetingReport.objects.filter(
        meeting_type=MEETING_TYPES_DICT['Business']
    ).order_by('meeting_date')
    return direct_to_template(request,
                              'meetings/index.html',
                              {'business':business_minutes,
                               'section':'meetings',
                               'special':[],
                               'worship':[]})

def add_report(request,meeting):
    """
    Adds a report to the including meeting.

    :param meeting: Name of meeting (Should be Business, Worship, or
                    Special.
    """
    if request.user.is_superuser and request.method == 'POST':
        if request.POST.has_key('authors'):
            authors = request.POST.get('authors')
        else:
            authors = []
        authors = [User.objects.get(pk=author) for author in authors]
        meeting_date = request.POST.get('meeting_date')
        meeting_type = MEETING_TYPES_DICT[meeting]
        report_type = request.POST.get('report_type')
        rst_filename = request.POST.get('rstFileLocation')
        new_report = MeetingReport(meeting_date=meeting_date,
                                   meeting_type=meeting_type,
                                   report_type=report_type,
                                   rstFileLocation=rst_filename)
        new_report.save()
        new_report.authors = authors
        new_report.save()
    return HttpResponseRedirect('/meetings/%s' % meeting)

def get_type(type_list,value):
    """
    Helper function takes a list of tuples and matches and returns
    integer

    :param type_list: Constant list of tuples used in models and views
    :param value: Value to match in second position of tuple
    """
    for row in type_list:
        if row[1] == value:
            return row[0]
    return None

def display_month(request,
                  meeting,
                  year,
                  month):
    meeting = meeting.lower()
    month = QUAKER_MONTHS[int(month)]
    cache_key = "{0}-{1}-month-{2}-meeting".format(year,month,meeting)
    html_cache = cache.get(cache_key)
    meeting_date = cache.get('{0}-date'.format(cache_key))
    if html_cache is None: 
        year_loader = get_year(year)
        if year_loader is not None:
            raw_html = year_loader["{0}-month".format(month)]["meetings"][meeting]["html"]
            meeting_date = year_loader["{0}-month".format(month)]["meetings"][meeting]["date"]
        else:
            raw_html = "Cannot find {0} {1} for {3}".format(month,year,meeting)
            meeting_date = None
        html_cache = raw_html
        cache.set(cache_key,html_cache)
        cache.set('{0}-date'.format(cache_key),meeting_date)
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return direct_to_template(request,
                              'meetings/report.html',
                              {'user':user,
                               'meeting':meeting,
                               'meeting_date':meeting_date,
                               'report_type':'Minutes',
                               'section':'meetings',
                               'contents':html_cache})

def display_report(request,
                   meeting,
                   year,
                   month,
                   report_name):
    """
    Displays a Meeting Minute, Special Minute, or other Report

    :param meeting: Name of meeting
    :param year: YYYY four year digit string
    :param month: MM 01-12 digit 
    :param report_name: Name of rst report (filename)
    :rtype: Generated HTML
    """
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return direct_to_template(request,
                              'meetings/report.html',
                              {'user':user,
                               'report':report,
                               'section':'meetings',
                               'contents':report_rst})
    

                                                
def display_year(request,
		 meeting,
		 year):
    """
    Displays all Minutes for a Year View
    """
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    minutes = list()
    meeting_key = meeting.lower()
    year_loader = get_year(str(year))
    for k,v in year_loader.iteritems():
        if v['meetings'].has_key(meeting_key):
            minutes.append(v['meetings'][meeting_key]['date'])
    meeting = {'name':'Meeting for Worship for {0}'.format(meeting),
               'minutes':sorted(minutes),
               'type_of':MEETING_TYPES_DICT[meeting]}
    return direct_to_template(request,
  		              'meetings/year.html',
			     {'minutes':minutes,
			      'meeting':meeting,
                              'user':user,
			      'year':year})

 

def advices_and_queries(request):
    """
    Advices and Queries View for Specific Committee
    """
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    advices,queries = [],[]
    # Extracts year from present
    today = datetime.today()
    year_loader = get_year(str(today.year))
    for k,v in year_loader.iteritems():
        if v["meetings"].has_key("advice"):
            advices.append(v['meetings']['advice']['date'])
        if v["meetings"].has_key("query"):
            queries.append(v['meetings']['query']['date'])
    return direct_to_template(request,
                              'meetings/advices-queries.html',
                              {'advices':sorted(advices),
                               'queries':sorted(queries),
                               'section':'meetings',
                               'user':user})

def business(request):
    """
    Displays Business Meeting view
    """
    minutes = list()
    today = datetime.today()
    year_loader = get_year(str(today.year))
    for k,v in year_loader.iteritems():
       if v['meetings'].has_key('business'):
           minutes.append(v['meetings']['business']['date'])
    
    minute_form = None
    if request.user.is_superuser:
        minute_form = MeetingReportForm()
    meeting = {'name':'Meeting for Worship for Business',
               'description':'A monthy meeting with a concern for business',
               'minutes':sorted(minutes),
               'type_of':MEETING_TYPES_DICT['Business']}
    return direct_to_template(request,
                              'meetings/meeting.html',
			      {'archive':ARCHIVE_YEARS,
			       'meeting':meeting,
                               'minute_form':minute_form,
                               'section':'meetings',})


def contact(request):
    """
    Displays Meeting's contact information
    """
    return direct_to_template(request,
                              "meetings/contact.html",
                              {'email_form':EmailContactForm()})

def special(request):
    """
    Displays Special Meeting view
    """
    minutes = list()
    today = datetime.today()
    year_loader = get_year(str(today.year))        
    for k,v in year_loader.iteritems():
       if v['meetings'].has_key('special'):
           minutes.append(v['meetings']['special']['date'])
    meeting = {'name':'Special Called Meeting',
               'description':'A meeting called for Friends regarding a special topic or concern',
               'minutes':sorted(minutes),
               'type_of':MEETING_TYPES_DICT['Special']}
    return direct_to_template(request,
                              'meetings/meeting.html',
                              {'meeting':meeting,
                               'section':'meetings'})

def worship(request):
    """
    Displays Worship Meeting view
    """
    meeting = {'name':'Meeting for Worship',
               'description':'A weekly meeting, usually held First Day, for shared communial worship in silence',
               'minutes':[],
               'type_of':MEETING_TYPES_DICT['Worship']}
    return direct_to_template(request,
                              'meetings/meeting.html',
                              {'meeting':meeting,
                               'section':'meetings',})    
    
