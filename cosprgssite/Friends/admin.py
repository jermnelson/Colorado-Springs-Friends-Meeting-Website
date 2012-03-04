"""
 :mod:`admin` Gives admin access to the Colorado Springs Meeting Friends Models
"""
__author__ = "Jeremy Nelson"

from Friends.models import *
from django.contrib import admin

admin.site.register(Friend)
