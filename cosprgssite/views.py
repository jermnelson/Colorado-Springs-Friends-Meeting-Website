"""
 :mod:`views` 
"""
__author__ = 'Jeremy Nelson'

import datetime
from calendar import HTMLCalendar
from django.http import Http404,HttpResponse
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.views.generic.simple import direct_to_template
from events.models import MeetingEvent
from donate.forms import PersonForm
from quakers.forms import EmailContactForm
import settings
import django_helpers
#from paypal.standard.forms import PayPalPaymentsForm

class Events(object):

    def __init__(self,**kwargs):
        self.events = []
        if 'meeting' in kwargs:
            self.events.append(kwargs.get('meeting'))

    def day_url(self,year,month,day,has_event=False):
        return ''

    def month_url(self,year,month):
        return ''

    def events_by_day(self,year,month):
        return dict()
                               

def email(request):
    """
    Default view for email receipt
    """
    if request.method != 'POST':
        raise Http404
    note = request.POST.get('message')
    return_email = request.POST.get('return_email')
    if len(return_email) < 1:
        return_email = 'Unknown'
    message = {'title':"Your Email Inquiry has been received",
               'body':'''We have received your email request and we will get back
    to you as soon as we are able. If you need more immediate assistance,
    please call 719-685-5548.'''}
    
    send_mail('Email from {0}'.format(return_email),
              note,
              settings.EMAIL_HOST_USER,
              ['jermnelson@gmail.com',],
              fail_silently=False)
    return direct_to_template(request,
                              'message.html',
                              {'message':message})
                              

def home(request):
    """
    Default view for Colorado Springs Monthly Meeting Website
    """
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    event_query = MeetingEvent.objects.all()
    events = Events()
    today = datetime.datetime.today()
    current_calendar = HTMLCalendar().formatmonth(today.year,today.month)
    paypal_dict = {"business":"jermnelson@gmail.com",
                   "amount":"0",
                   "item_name":"Online donation",
                   "notify_url":"",
                   "return_url":"",
                   "cancel_return":""}
    #paypal_form = PayPalPaymentsForm(initial=paypal_dict)
    return direct_to_template(request,
                              'index.html',
                             {'current_calendar':current_calendar,
                              'email_form':EmailContactForm(),
                             # 'person_form':paypal_form,
                              'person_form':PersonForm(),
                              'section':'testimonies',
                              'user':user})

def reload_rst(request):
    """
    Reloads RST files from static directories
    """
    if not request.user.is_authenticated() or request.method != 'POST':
        raise Http404
    #django_helpers.reload_years()
    return HttpResponse("Reloaded RST files")
    
