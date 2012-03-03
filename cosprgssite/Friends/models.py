"""
 :mod:`models` Data models for Colorado Springs Quaker Meeting Friends
"""
from django.db import models

# Create your models here.
class Friend(models.model):
    user = models.ForeignKey(User)

