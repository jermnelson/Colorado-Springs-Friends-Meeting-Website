"""
 :mod:`models` Friends models for Colorado Springs Quaker Meeting 
"""
__author__ = 'Jeremy Nelson'

from django.db import models
from django.contrib.auth.models import User
from location.models import Address,Location

class Friend(models.Model):
    additional_name = models.CharField(max_length=60,blank=True)
    address = models.ForeignKey(Address,related_name="friend_address")
    birth_day = models.DateField(blank=True)
    initials = models.CharField(max_length=10,blank=True)
    gender = models.CharField(max_length=30,blank=True)
    location = models.ForeignKey(Location,blank=True,related_name="friend_location")
    nickname = models.CharField(max_length=10,blank=True)
    maiden_name = models.CharField(max_length=60,blank=True)
    prefix = models.CharField(max_length=15,blank=True)
    short_name = models.CharField(max_length=30,blank=True)
    user = models.ForeignKey(User)
    suffix = models.CharField(max_length=15,blank=True)
    yomi_additional_name = models.CharField(max_length=60,blank=True)
    yomi_given_name = models.CharField(max_length=60,blank=True)
    yomi_family_name = models.CharField(max_length=60,blank=True)
    yomi_name = models.CharField(max_length=60,blank=True)
    

