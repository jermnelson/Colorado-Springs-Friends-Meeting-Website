"""
 :mod:`views` Colorado Springs Quaker Meeting Friends View
"""
__author__ = 'Jeremy Nelson'
from django.http import HttpResponse

def default(request):
    return HttpResponse("NEEDS DESIGN -- Index page for Friends")

def friend(request,username):
    return HttpResponse("NEEDS DETAIL view for %s" % username)

def young_friends(request):
    return HttpResponse("NEEDS DESIGN -- Young Friends")


