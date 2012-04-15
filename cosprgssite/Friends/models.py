"""
 :mod:`models` Friends models for Colorado Springs Quaker Meeting 
"""
__author__ = 'Jeremy Nelson'

from django.db import models
from django.contrib.auth.models import User
from location.models import Address,Location
from django.db.models.signals import post_save

class Friend(models.Model):
    additional_name = models.CharField(max_length=60,blank=True,null=True)
    address = models.ForeignKey(Address,
                                related_name="friend_address",
                                blank=True,
                                null=True)
    birth_day = models.DateField(blank=True,null=True)
    
    initials = models.CharField(max_length=10,blank=True,null=True)
    gender = models.CharField(max_length=30,blank=True,null=True)
    location = models.ForeignKey(Location,
                                 blank=True,
                                 null=True,
                                 related_name="friend_location")
    nickname = models.CharField(max_length=10,blank=True,null=True)
    maiden_name = models.CharField(max_length=60,blank=True,null=True)
    prefix = models.CharField(max_length=15,blank=True,null=True)
    short_name = models.CharField(max_length=30,blank=True,null=True)
    suffix = models.CharField(max_length=15,blank=True,null=True)
    user = models.ForeignKey(User,unique=True)
    yomi_additional_name = models.CharField(max_length=60,blank=True)
    yomi_given_name = models.CharField(max_length=60,blank=True,null=True)
    yomi_family_name = models.CharField(max_length=60,blank=True,null=True)
    yomi_name = models.CharField(max_length=60,blank=True,null=True)


    
##def create_user_profile(sender, instance, created, **kwargs):
##    if created is not None:
##        Friend.objects.create(user=instance)

##post_save.connect(create_user_profile, sender=User)
