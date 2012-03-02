"""
 :mod:views Colorado Springs Friends Meeting Committee View
"""
__author__ = "Jeremy Nelson"
from django.contrib.auth import authenticate
from django.views.generic.simple import direct_to_template

def display_report(request,
                   year,
                   month,
                   day,
                   report_name):
     """
     Function displays a reStructured Committee report

     :param year: YYYY four year digit string
     :param month: MM 01-12 digit 
     :param day: DD 01-31 digit
     :param report_name: Name of rst report (filename)
     :rtype: Generated HTML
     """
     return direct_to_template(request,
                               'committees/report.html',
                               {})
