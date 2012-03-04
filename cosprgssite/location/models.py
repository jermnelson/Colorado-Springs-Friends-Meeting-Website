"""
 :mod:`model` Location data models for Colorado Springs Quaker Meeting Friends
"""

from django.db import models



class Location(models.Model):
    name = models.CharField(max_length=255)
    parent_location = models.ForeignKey('self',blank=True)

class Address(Location):
    city = models.ForeignKey(Location,related_name="city_address")
    mail_code = models.CharField(verbose_name="Zip Code",
                                 max_length=20,
                                 blank=True)
    state = models.ForeignKey(Location,related_name="state_address")
    street = models.CharField(max_length=255)
    
