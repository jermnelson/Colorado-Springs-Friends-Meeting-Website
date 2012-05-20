"""
 :mod:`forms` Colorado Springs Quaker Meeting Committee Forms
"""
from committees.models import *
from django.forms import *

class CommitteeForm(ModelForm):
    class Meta:
        model=Committee


class CommitteeReportForm(ModelForm):
    class Meta:
        model=CommitteeReport

class CommitteeFriendChoiceField(ModelChoiceField):
    def label_from_instance(self,obj):
        return obj.friend.short_name

class CommitteeMemberForm(ModelForm):
    class Meta:
        model=CommitteeMember

class OfficerForm(ModelForm):
    class Meta:
        model=Officer

