from django.db import models
from Friends.models import Friend
from committees.models import Committee
from meetings.models import MEETING_TYPES

class Event(models.Model):
    created_by = models.ForeignKey(Friend,related_name='Created by')
    created_on = models.DateTimeField(auto_now=True,auto_now_add=True)
    description = models.CharField(max_length=255,blank=True,null=True)
    end_on = models.DateTimeField(blank=True,null=True)
    friends = models.ManyToManyField(Friend)
    name = models.CharField(max_length=50)
    start_on = models.DateTimeField()
    
class CommitteeEvent(Event):
    committee = models.ForeignKey(Committee)

class MeetingEvent(Event):
    meeting_type = models.IntegerField(choices=MEETING_TYPES)
    

