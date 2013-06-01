"""
 mod:`views` Quaker Donation Views
"""
__author__ = 'Jeremy Nelson'

from django.shortcuts import render

from forms import PersonForm

def default(request):
    """
    Displays default view for donation page
    """
    return render(request,
                  'donate/index.html',
                  {'person_form':PersonForm()})
