__author__ = "Jeremy Nelson"

import os

from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from cosprgssite.settings import PROJECT_HOME
from friends.models import Friend, CommitteeMembership

def default(request):
    if request.user.is_authenticated:
        friends = Friend.objects.all()
    else:
        friends = Friend.objects.all().filter(is_public=True)
    return render(request,
                  'friends.html',
                  {'category': 'about',
                   'friends': friends,
                   'section': 'friend'})

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
    friend = Friend.objects.all().get(user=user_query[0])
    if not request.user.is_authenticated():
        if not friend.is_public:
            raise Http404
    committees = CommitteeMembership.objects.all().filter(friend=friend)
    if not os.path.exists(custom_template):
        custom_template = 'friend.html'
    return render(request,
                  custom_template,
                  {'category': 'about',
                   'committees': committees,
                   'info': friend,
                   'section': 'friend',
                   'username': username})
    
