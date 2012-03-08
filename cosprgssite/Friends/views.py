"""
 :mod:`views` Colorado Springs Quaker Meeting Friends View
"""
__author__ = 'Jeremy Nelson'
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader, TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
from Friends.forms import FriendForm
from Friends.models import Friend

def default(request):
    return HttpResponse("NEEDS DESIGN -- Index page for Friends")

def display_friend(request,username):
    template_name = 'Friends/%s.html' % username
    try:
        template = loader.get_template('Friends/%s.html' % username)
    except TemplateDoesNotExist:
        template_name = 'Friends/person.html'
    return direct_to_template(request,
                              template_name,
                              {'friend':{'username':username}})

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


