"""
 :mod:`model` Location data models for Colorado Springs Quaker Meeting Friends
"""

from django.db import models



class Location(models.Model):
    name = models.CharField(max_length=255)
    parent_location = models.ForeignKey('self',blank=True)

class Address(models.Model):
    city = models.CharField(max_length=120)
##    city = models.ForeignKey(Location,related_name="city_address")
    md5_key = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=32)
##    state = models.ForeignKey(Location,related_name="state_address")
    state = models.CharField(max_length=50)
    street = models.CharField(max_length=255)
    
    
