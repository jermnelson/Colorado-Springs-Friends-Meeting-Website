"""
 :mod:`admin` Gives admin access to the Colorado Springs Meeting Committee Models
"""
__author__ = "Jeremy Nelson"

from meetings.models import *
from django.contrib import admin

admin.site.register(MeetingReport)
admin.site.register(MeetingEvent)

