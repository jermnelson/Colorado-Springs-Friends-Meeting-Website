"""
 :mod:`forms` Colorado Springs Quaker Meeting Committee Forms
"""
from committees.models import *
from django.forms import ModelForm

class CommitteeForm(ModelForm):
    class Meta:
        model=Committee

class CommitteeReportForm(ModelForm):
    class Meta:
        model=CommitteeReport

class CommitteeMemberForm(ModelForm):
    class Meta:
        model=CommitteeMember

class OfficerForm(ModelForm):
    class Meta:
        model=Officer

