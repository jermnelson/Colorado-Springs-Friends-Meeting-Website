"""
 mod:`views` Quaker Donation Views
"""
__author__ = 'Jeremy Nelson'

from django.views.generic.simple import direct_to_template

def default(request):
    """
    Displays default view for donation page
    """
    return direct_to_template(request,
                              'donate/index.html',
                              {})
