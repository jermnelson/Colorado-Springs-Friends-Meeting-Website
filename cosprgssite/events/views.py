__author__ = "Jeremy Nelson"

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.generic.simple import direct_to_template

def default(request):
    return direct_to_template(request,
                              'events/index.html',
                              {})
