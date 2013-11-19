__author__ = "Jeremy Nelson"

from django.db import models
from django.contrib.auth.models import Group, User

class Category(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return unicode(self.name)

class Committee(models.Model):
    dateCreated = models.DateField(blank=True, null=True)
    datePutDown = models.DateField(blank=True, null=True)
    group = models.OneToOneField(Group)
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return unicode(self.name)

class CommitteeMembership(models.Model):
    committee = models.ForeignKey('Committee')
    dateCompleted = models.DateField(blank=True, null=True)
    dateStarted = models.DateField()
    friend = models.ForeignKey('Friend')
    is_clerk = models.BooleanField(default=False)
    is_recorder = models.BooleanField(default=False)

    def __unicode__(self):
        return u"{0} -- {1}".format(
            self.committee.name,
            self.friend.user.username)
    
class Friend(models.Model):
    birthday = models.DateField(blank=True,
                                null=True)
    category = models.ForeignKey('Category')
    parent = models.ManyToManyField('self',
                                     blank=True,
                                     related_name='friend_sibling',
                                     null=True)
    is_birthright = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    postal_address = models.ForeignKey('PostalAddress',
                                      blank=True,
                                      null=True)
    sibling = models.ManyToManyField('self',
                                     blank=True,
                                     related_name='friend_sibling',
                                     null=True)
    spouse = models.ForeignKey('self',
                               blank=True,
                               related_name='friend_spouse',
                               null=True)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

class OfficeHolder(models.Model):
    dateCompleted = models.DateField(blank=True, null=True)
    dateStarted = models.DateField()
    friend = models.ForeignKey('Friend')
    office = models.CharField(max_length=30)

    def __unicode__(self):
        return "{0} - {1}".format(self.office,
                                  self.friend.user.username)

class PhoneNumber(models.Model):
    number_types = [(0,'Home'),
                    (1,'Cell'),
                    (2,'Business'),
                    (3,'Work'),
                    (4,'Other')]
    number = models.CharField(max_length=30)
    friends = models.ManyToManyField(Friend)
    phone_number_type = models.IntegerField(default=0,
                                            choices=number_types)

    def __unicode__(self):
        return unicode(self.number)
    
class PostalAddress(models.Model):
    addressLocality = models.CharField(blank=True, null=True, max_length=60)
    addressRegion = models.CharField(blank=True, null=True, max_length=60)
    postalCode = models.CharField(blank=True, null=True, max_length=60)
    streetAddress = models.CharField(blank=True, null=True, max_length=60)

    def __unicode__(self):
        return u"{0}, {1} {2}".format(
            self.streetAddress,
            self.addressLocality,
            self.addressRegion)
