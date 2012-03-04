"""
 :mod:`admin` Gives admin access to the Colorado Springs Meeting Committee Models
"""
__author__ = "Jeremy Nelson"

from committees.models import *
from django.contrib import admin

admin.site.register(Committee)
admin.site.register(CommitteeMember)
admin.site.register(CommitteeReport)
admin.site.register(Position)

