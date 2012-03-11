"""
 :mod:`models` Django supporting models for Meetings
"""
__author__ = "Jeremy Nelson"
from django.db import models
from django.contrib.auth.models import User

MEETING_TYPES = ((1,"Business"),
                 (2,"Worship"),
                 (3,"Special"))

OFFICER_TYPES = ((1,"Clerk"),
                 (2,"Recording Clerk"),
                 (3,"Treasurer"))

REPORT_TYPES = ((1,"Minutes"),
                (2,"Report"),
                (3,"Advice"),
                (4,"Query"),
                (5,"State of the Meeting"))


class MeetingOfficer(models.Model):
    date_started = models.DateField()
    date_finished = models.DateField(blank=True,null=True)
    friend = models.ForeignKey(User)
    officer = models.IntegerField(choices=OFFICER_TYPES)

class MeetingReport(models.Model):
    authors = models.ManyToManyField(User)
    meeting_date = models.DateTimeField()
    description = models.TextField(blank=True,null=True)
    ingested_date = models.DateTimeField(auto_now=True,
                                         auto_now_add=True)
    meeting_type = models.IntegerField(choices=MEETING_TYPES)
    rstFileLocation = models.CharField(max_length=255)
    report_type = models.IntegerField(choices=REPORT_TYPES)

