"""
 :mod:models Django supporting models for Committee
"""
__author__ = 'Jeremy Nelson'


from django.db import models
from django.contrib.auth.models import User


QUAKER_MONTHS = {'01':'first-month',
                 '02':'second-month',
                 '03':'third-month',
                 '04':'forth-month',
                 '05':'fifth-month',
                 '06':'sixth-month',
                 '07':'seventh-month',
                 '08':'eight-month',
                 '09':'ninth-month',
                 '10':'tenth-month',
                 '11':'eleventh-month',
                 '12':'twelfth-month'}

REPORT_TYPES = ((1,"Advice and Queries"),
                (2,"Minute"),
                (3,"Special Minute"),
                (4,"Agenda"),
                (5,"Cash flow"),
                (6,"Balance sheet"))



class Committee(models.Model):
    date_created = models.DateTimeField(auto_now=True,
                                        auto_now_add=True)
    name = models.CharField(max_length=150)
    

class CommitteeMember(models.Model):
    committee = models.ForeignKey(Committee)
    user = models.ForeignKey(User)
    date_joined = models.DateField()
    date_left = models.DateField(blank=True,null=True)
    
    
class Officer(models.Model):
    committee_member = models.ForeignKey(CommitteeMember)
    date_ended = models.DateField(blank=True,null=True)
    date_started = models.DateField()
    value = models.CharField(max_length=45)
    
                     
class CommitteeReport(models.Model):
    authors = models.ManyToManyField(CommitteeMember)
    committee = models.ForeignKey(Committee)
    ingested_date = models.DateTimeField(auto_now=True,
                                         auto_now_add=True)
    rstFileLocation = models.CharField(max_length=255)
    report_date = models.DateTimeField()
    report_type = models.IntegerField(choices=REPORT_TYPES)
    




