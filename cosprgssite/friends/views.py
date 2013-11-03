__author__ = "Jeremy Nelson"

import os

from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from cosprgssite.settings import PROJECT_HOME
from friends.models import Friend

def friend(request,
           username):
    custom_template = os.path.join(PROJECT_HOME,
                                   'cosprgssite',
                                   'templates',
                                   '{0}.html'.format(username))
    if username.endswith("/"):
        username = username[:-1]
    user_query = User.objects.all().filter(username=username)
    if len(user_query) < 1:
        raise Http404
    info = Friend.objects.all().get(user=user_query[0])
    if not os.path.exists(custom_template):
        custom_template = 'friend.html'
    return render(request,
                  custom_template,
                  {'category': 'about',
                   'info': info,
                   'section': 'friend',
                   'username': username})
    
