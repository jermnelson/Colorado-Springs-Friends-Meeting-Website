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
    category = models.ForeignKey('FriendCategory',blank=True,null=True)
    birth_day = models.DateField(blank=True,null=True)
    
    initials = models.CharField(max_length=10,blank=True,null=True)
    gender = models.CharField(max_length=30,blank=True,null=True)
    location = models.ForeignKey(Location,
                                 blank=True,
                                 null=True,
                                 related_name="friend_location")
    nickname = models.CharField(max_length=10,blank=True,null=True)
    maiden_name = models.CharField(max_length=60,blank=True,null=True)
    md5_key = models.CharField(max_length=32)
    prefix = models.CharField(max_length=15,blank=True,null=True)
    short_name = models.CharField(max_length=30,blank=True,null=True)
    suffix = models.CharField(max_length=15,blank=True,null=True)
    user = models.ForeignKey(User,unique=True)
    young_friend = models.NullBooleanField(blank=True,null=True)
    yomi_additional_name = models.CharField(max_length=60,blank=True)
    yomi_given_name = models.CharField(max_length=60,blank=True,null=True)
    yomi_family_name = models.CharField(max_length=60,blank=True,null=True)
    yomi_name = models.CharField(max_length=60,blank=True,null=True)

class FriendCategory(models.Model):
    code = models.CharField(max_length=5)
    friends = models.ManyToManyField(Friend)
    label = models.CharField(max_length=155)
    

class FriendPhoneNumbers(models.Model):
    number = models.CharField(max_length=30)
    phone_number_type = models.IntegerField(default=0,
                                            choices=[(0,'Home'),
                                                     (1,'Cell'),
                                                     (2,'Business'),
                                                     (3,'Other')])
    user = models.ForeignKey(User)
    
##def create_user_profile(sender, instance, created, **kwargs):
##    if created is not None:
##        Friend.objects.create(user=instance)

##post_save.connect(create_user_profile, sender=User)
