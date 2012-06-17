"""
  :mod:`views` Views for Meetings 
"""
__author__ = 'Jeremy Nelson'
import logging
from datetime import datetime
from django.contrib.auth import authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from meetings.forms import MeetingReportForm
from meetings.models import MEETING_TYPES, REPORT_TYPES, MeetingReport
#from committees.views import get_report
from django_helpers import build_loader,year2011,year2012

from django.contrib.auth.models import User

MEETING_TYPES_DICT = {}
for row in MEETING_TYPES:
    MEETING_TYPES_DICT[row[1]] = row[0]



def default(request):
    """
    Default view for Meetings
    """
    business_minutes = MeetingReport.objects.filter(
        meeting_type=MEETING_TYPES_DICT['Business']
    ).order_by('meeting_date')
    logging.error("business minutes %s" % business_minutes)
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
    if year == '2011':
        raw_html = year2011["{0}-month".format(month)]["meetings"][meeting]["html"]
        meeting_date = year2011["{0}-month".format(month)]["meetings"][meeting]["date"]
    elif year == '2012':
        raw_html = year2012["{0}-month".format(month)]["meetings"][meeting]["html"]
        meeting_date = year2012["{0}-month".format(month)]["meetings"][meeting]["date"]
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
                               'contents':raw_html})

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
    

                                                
        

def advices_and_queries(request):
    """
    Advices and Queries View for Specific Committee
    """
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    advices = []
    queries = []
    return direct_to_template(request,
                              'meetings/advices-queries.html',
                              {'advices':advices,
                               'queries':queries,
                               'section':'meetings',
                               'user':user})

def business(request):
    """
    Displays Business Meeting view
    """
    minutes = list()
    for k,v in year2012.iteritems():
       print(v)
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
                              {'meeting':meeting,
                               'minute_form':minute_form,
                               'section':'meetings',})


def contact(request):
    """
    Displays Meeting's contact information
    """
    return direct_to_template(request,
                              "meetings/contact.html")

def special(request):
    """
    Displays Special Meeting view
    """
    meeting = {'name':'Special Called Meeting',
               'description':'A meeting called for Friends regarding a special topic or concern',
               'minutes':[],
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
    
