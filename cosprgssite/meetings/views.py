"""
  :mod:`views` Views for Meetings 
"""
__author__ = 'Jeremy Nelson'
from django.contrib.auth import authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from meetings.forms import MeetingReportForm
from meetings.models import MEETING_TYPES, MeetingReport

MEETING_TYPE_DICT = {}
for row in MEETING_TYPES:
    MEETING_TYPE_DICT[row[1]] = row[0]

def default(request):
    """
    Default view for Meetings
    """
    return direct_to_template(request,
                              'meetings/index.html',
                              {'business':[],
                               'special':[],
                               'worship':[]})

def advices_and_queries(request):
    """
    Advices and Queries View for Specific Committee
    """
    return HttpResponse("NEEDS IMPLEMENTATION - advices and queries")

def business(request):
    """
    Displays Business Meeting view
    """
    minutes = MeetingReport.objects.filter(report_type=MEETING_TYPES_DICT['business'])
    minute_form = None
    if request.user.is_superuser:
        minute_form = MeetingReportForm()
    meeting = {'name':'Meeting for Worship for Business',
               'description':'A monthy meeting with a concern for business',
               'minutes':minutes,
               'type_of':MEETING_TYPES_DICT['business']}
    return direct_to_template(request,
                              'meetings/meeting.html',
                              {'meeting':meeting,
                               'minute_form':minute_form})


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
               'type_of':MEETING_TYPES_DICT['special']}
    return direct_to_template(request,
                              'meetings/meeting.html',
                              {'meeting':meeting})

def worship(request):
    """
    Displays Worship Meeting view
    """
    meeting = {'name':'Meeting for Worship',
               'description':'A weekly meeting, usually held First Day, for shared communial worship in silence',
               'minutes':[],
               'type_of':MEETING_TYPES_DICT['worship']}
    return direct_to_template(request,
                              'meetings/meeting.html',
                              {'meeting':meeting})

 
def add_report(request,meeting_type):
    """
    Adds a report for a Meeting
    """
    if request.method == 'POST' and request.user.is_superuser:
        new_report = MeetingReport()
    return HttpResponseRedirect('/meetings/%s' % meeting_type)
    
    
