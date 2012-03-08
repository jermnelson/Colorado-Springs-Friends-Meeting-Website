"""
 :mod:`views` Colorado Springs Quaker Meeting Friends View
"""
__author__ = 'Jeremy Nelson'
from django.http import HttpResponse
from django.template import loader, TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

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

def young_friends(request):
    return HttpResponse("NEEDS DESIGN -- Young Friends")


