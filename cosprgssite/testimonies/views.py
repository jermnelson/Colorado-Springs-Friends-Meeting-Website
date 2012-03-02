"""
  :mod:`views` Views for Testimonies
"""
__author__ = 'Jeremy Nelson'
from django.contrib.auth import authenticate
from django.views.generic.simple import direct_to_template


def community(request):
    pass

def default(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return direct_to_template(request,
                              'testimonies/index.html',
                              {'user':user,
                               'page':{'name':'Quaker Testimonies at Colorado Springs Friends Meeting',
                                       'description':'''The Quaker Testimonies
                                                        of Simplicity, Peace,
                                                        Integrity/Truth,
                                                        Community, and
                                                        Equality play a vital
                                                        role in the life of the
                                                        meeting'''}
                                       })
                               

def equality(request):
    pass

def integrity(request):
    pass


def peace(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return direct_to_template(request,
                              'testimonies/peace.html',
                              {'user':user,
                               'page':{'name':'Quaker Peace Testimony'}})

def simplicity(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return direct_to_template(request,
                              'testimonies/simplicity.html',
                              {'user':user,
                               'page':{'name':'Quaker Simplicity Testimony'}})


def truth(request):
    pass
