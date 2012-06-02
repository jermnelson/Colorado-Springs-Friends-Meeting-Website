"""
 :mod:`admin` Gives admin access to the Colorado Springs Meeting Committee Models
"""
__author__ = "Jeremy Nelson"

from events.models import *
from django.contrib import admin

admin.site.register(Event)
admin.site.register(MeetingEvent)
admin.site.register(CommitteeEvent)

