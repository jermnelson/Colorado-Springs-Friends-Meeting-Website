"""
 :mod:`views` Colorado Springs Quaker Meeting Friends View
"""
__author__ = 'Jeremy Nelson'
import sys,logging
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader, TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
from committees.models import CommitteeMember
from Friends.forms import FriendForm
from Friends.models import Friend,FriendCategory

@login_required
def census(request):
    friend_query = Friend.objects.all().order_by('user__last_name')
    friends = []
    for friend in friend_query:
        friends.append(friend)
   # friends = sorted(friends,key=lambda x: x.user.last_name)
    shard_one = friends[0:len(friends)/2]
    shard_two = friends[len(friends)/2:]
    return direct_to_template(request,
                              'Friends/census.html',
                              {'friends':friends,
                               'categories':FriendCategory.objects.all().order_by('code'),
                               'shard_one':shard_one,
                               'shard_two':shard_two,
                               'year': 2012})

def default(request):
    return HttpResponse("NEEDS DESIGN -- Index page for Friends")

def display_friend(request,username):
    template_name = 'Friends/%s.html' % username
    try:
        template = loader.get_template('Friends/%s.html' % username)
        return direct_to_template(request,
                                  template_name,
                                  {})
                                  
    except TemplateDoesNotExist:
        template_name = 'Friends/person.html'
    user_query = User.objects.filter(username=username)
    friend,committees = None,[]
    if len(user_query) == 1:
        friend_user = user_query[0]
        friend_query = Friend.objects.filter(user=friend_user)
        if len(friend_query) > 0:
            friend = friend_query[0]
        else:
            friend = friend_user
        committee_query = CommitteeMember.objects.filter(user=friend_user)
        logging.error(type(committee_query))
        if len(committee_query) > 0:
            committees = committee_query
    return direct_to_template(request,
                              template_name,
                              {'committees':committees,
                               'friend':friend})

def display_profile(request):
    if request.user.is_authenticated():
        friend_query = Friend.objects.filter(user=request.user)
        if friend_query:
            friend_form = FriendForm(instance=friend_query[0])
        else:
            friend_form = FriendForm()
        return direct_to_template(request,
                                  'Friends/profile.html',
                                  {'form':friend_form,
                                   'friend':request.user})
    else:
        return HttpResponseRedirect("/accounts/login/")
        

def young_friends(request):
    return HttpResponse("NEEDS DESIGN -- Young Friends")


