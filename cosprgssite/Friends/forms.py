"""
 :mod:`forms` Colorado Springs Quaker Meeting Friends Form
"""
__author__ = "Jeremy Nelson"
from Friends.models import Friend
from django.forms import ModelForm

class FriendForm(ModelForm):
    class Meta:
        model = Friend
