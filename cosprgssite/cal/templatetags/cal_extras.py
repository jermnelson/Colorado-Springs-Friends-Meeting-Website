"""
 :mod:views Colorado Springs Friends Calendar extras, forked source from 
 djangoEventCal app.
"""
__author__ = "Jeremy Nelson"

import logging
from django.template import Context,Library,loader
from django.utils.safestring import mark_safe

register = Library()

def getWeekHeader(calendar):
    """return a list of week header"""
    return calendar.weekheader(2).split()

def getMonthHeader(current):
    """return a tuple that contains abbv. month name and 4 digit year"""
    return current.getDate(1).strftime("%b"), current.year

register.filter('getWeekHeader',getWeekHeader)
register.filter('getMonthHeader',getMonthHeader)
