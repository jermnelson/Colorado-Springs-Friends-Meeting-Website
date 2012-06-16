"""
  :mod:`views` Views for Testimonies
"""
__author__ = 'Jeremy Nelson'
from django.contrib.auth import authenticate
from django.views.generic.simple import direct_to_template


def community(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return direct_to_template(request,
                              'testimonies/community.html',
                              {'user':user,
                               'section':'testimonies',
                               'page':{'name':'Quaker Community Testimony',
                                       'title':'Colorado Springs Quaker Meeting - Community Testimony'}})

def default(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return direct_to_template(request,
                              'testimonies/index.html',
                              {'user':user,
                               'section':'testimonies',
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
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return direct_to_template(request,
                              'testimonies/equality.html',
                              {'user':user,
                               'section':'testimonies',
                               'page':{'name':'Quaker Equality Testimony',
                                       'title':'Colorado Springs Quaker Meeting - Equality Testimony'}})

def integrity(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return direct_to_template(request,
                              'testimonies/integrity.html',
                              {'user':user,
                               'section':'testimonies',
                               'page':{'name':'Quaker Integrity and Truth Testimony',
                                       'title':'Colorado Springs Quaker Meeting - Integrity Testimony'}})


def peace(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return direct_to_template(request,
                              'testimonies/peace.html',
                              {'user':user,
                               'section':'testimonies',
                               'page':{'name':'Quaker Peace Testimony',
                                       'title':'Colorado Springs Quaker Meeting - Peace Testimony'}})

def simplicity(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return direct_to_template(request,
                              'testimonies/simplicity.html',
                              {'user':user,
                               'section':'testimonies',
                               'page':{'name':'Quaker Simplicity Testimony',
                                       'title':'Colorado Springs Quaker Meeting - Simplicity Testimony'}})


def truth(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return direct_to_template(request,
                              'testimonies/integrity.html',
                              {'user':user,
                               'section':'testimonies',
                               'page':{'name':'Quaker Integrity and Truth Testimony'}})
