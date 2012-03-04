"""
 :mod:`admin` Gives admin access to the Colorado Springs Meeting location Models
"""
__author__ = "Jeremy Nelson"

from location.models import *
from django.contrib import admin

admin.site.register(Address)
admin.site.register(Location)

