"""
 :mod:views Colorado Springs Friends Meeting Committee View
"""
__author__ = "Jeremy Nelson"

import logging
from django.template import Context,Library,loader
from django.utils.safestring import mark_safe
from committees.models import REPORT_TYPES

register = Library()

report_types = {}
for choice in REPORT_TYPES:
    report_types[choice[0]] = choice[1]

def get_report_type(report_int):
    """
    Quick filter for returning text for a report type

    :param report_int: Stored integer in datastrore
    :rtype string:
    """
    if report_types.has_key(report_int):
        return mark_safe(report_types[report_int])
    else:
        return mark_safe("Report type %s not found" % report_int)

def pretty_month(month_int):
    if int(month_int) < 10:
        return mark_safe('0%s' % month_int)
    else:
        return mark_safe(month_int)

register.filter('get_report_type',get_report_type)
register.filter('pretty_month',pretty_month)

    
