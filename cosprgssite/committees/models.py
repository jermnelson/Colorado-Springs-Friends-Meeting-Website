"""
 :mod:models Django supporting models for Committee
"""
__author__ = 'Jeremy Nelson'


from django.db import models
from django.contrib.auth.models import User
from Friends.models import Friend

class Committee(models.Model):
    date_created = models.DateTimeField()
    name = models.CharField(max_length=150)
    members = models.ManyToManyField('CommitteeMember')

class CommitteeMember(models.Model):
    user = models.ForeignKey(Friend,unique=True)
    date_joined = models.DateField()
    date_left = models.DateField(blank=True,null=True)
    
    
class Position(models.Model):
    committee_member = models.ForeignKey(CommitteeMember)
    date_ended = models.DateField(blank=True,null=True)
    date_started = models.DateField()
    value = models.CharField(max_length=45)
    
                     
class CommitteeReport(models.Model):
    authors = models.ManyToManyField(CommitteeMember)
    committee = models.ForeignKey(Committee)
    ingested_date = models.DateTimeField(auto_now=True,
                                         auto_now_add=True)
    rstFileLocation = models.FilePathField(path=None)
    report_date = models.DateTimeField()
    




