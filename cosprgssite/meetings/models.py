"""
 :mod:`models` Django supporting models for Meetings
"""
__author__ = "Jeremy Nelson"
from django.db import models
from django.contrib.auth.models import User

MEETING_TYPES = ((1,"Business"),
                 (2,"Worship"),
                 (3,"Special"))

REPORT_TYPES = ((1,"Minute"),
                (2,"Report"),
                (3,"Advice"),
                (4,"Query"),
                (5,"State of the Meeting"))


class MeetingReport(models.Model):
    authors = models.ManyToManyField(User)
    meeting_date = models.DateTimeField()
    description = models.TextField(blank=True,null=True)
    ingested_date = models.DateTimeField(auto_now=True,
                                         auto_now_add=True)
    meeting_type = models.IntegerField(choices=MEETING_TYPES)
    rstFileLocation = models.CharField(max_length=255)
    report_type = models.IntegerField(choices=REPORT_TYPES)

