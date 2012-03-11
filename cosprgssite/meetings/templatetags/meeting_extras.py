"""
 :mod:views Colorado Springs Friends Meeting extras
"""
__author__ = "Jeremy Nelson"

import logging
from django.template import Context,Library,loader
from django.utils.safestring import mark_safe
from meetings.models import MEETING_TYPES, REPORT_TYPES
from committees.templatetags.committee_extras import pretty_month

register = Library()


def quick_filter(src_tuples,value):
    """
    Helper function iterates through source tuples and compares
    the value to the first postion

    :param src_tuples: Value of source tuples
    :param value: Integer
    :rtype String: Matched value from source
    """
    for row in src_tuples:
        if row[0] == int(value):
            return row[1]
    return None
    

def get_name(meeting_int):
    """
    Quick filter for returning name for a meeting type

    :param meeting_int: Stored integer in datastrore
    :rtype string:
    """
    meeting_name = quick_filter(MEETING_TYPES,meeting_int)
    if meeting_name is not None:
        return mark_safe(meeting_name)
    return mark_safe("%s Meeting Not found" % meeting_int)


def get_report(report_int):
    """
    Quick fitler for returning name for a report type.

    :param report_int: Stored integer in datastrore
    :rtype string:
    """
    report_name = quick_filter(REPORT_TYPES,report_int)
    if report_name is not None:
        return mark_safe(report_name)
    return mark_safe("%s Report type not found" % report_int)

register.filter('get_name',get_name)
register.filter('get_report',get_report)
register.filter('pretty_month',pretty_month)
    
