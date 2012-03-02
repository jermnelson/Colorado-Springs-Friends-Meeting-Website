"""
 :mod:models Django supporting models for Committee
"""
__author__ = 'Jeremy Nelson'


from django.db import models


class CommitteeReportAuthor(models.Model):
    user = User()

class CommitteeReports(models.Model):
    authors = models.ManyToManyKey(CommitteeAuthor)
    ingested_date = models.DateTimeField(auto_now=True,
                                         auto_now_add=True)
    rstFileLocation = models.CharField(max_length=255)
    report_date = models.DateTimeField()
    




