"""
 :mod:`forms` Colorado Springs Quaker Meeting Forms
"""
from meetings.models import *
from django.forms import ModelForm

class MeetingReportForm(ModelForm):
    class Meta:
        model=MeetingReport
