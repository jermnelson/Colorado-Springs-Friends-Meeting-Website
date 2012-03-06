"""
  :mod:`views` Views for Meetings 
"""
__author__ = 'Jeremy Nelson'
from django.contrib.auth import authenticate
from django.views.generic.simple import direct_to_template

def default(request):
    """
    Default view for Meetings
    """
    return direct_to_template(request,
                              'meetings/index.html',
                              {'business':[],
                               'special':[],
                               'worship':[]})

def business(request):
    """
    Displays Business Meeting view
    """
    meeting = {'name':'Meeting for Worship for Business',
               'description':'A monthy meeting with a concern for business',
               'minutes':[]}
    return direct_to_template(request,
                              'meetings/meeting.html',
                              {'meeting':meeting})

def special(request):
    """
    Displays Special Meeting view
    """
    meeting = {'name':'Special Called Meeting',
               'description':'A special meeting called for Friends regarding a special topic or concern',
               'minutes':[]}
    return direct_to_template(request,
                              'meetings/meeting.html',
                              {'meeting':meeting})

def worship(request):
    """
    Displays Worship Meeting view
    """
    meeting = {'name':'Meeting for Worship',
               'description':'A weekly meeting, usually held First Day, for shared communial worship in silent',
               'minutes':[]}
    return direct_to_template(request,
                              'meetings/meeting.html',
                              {'meeting':meeting})

 
