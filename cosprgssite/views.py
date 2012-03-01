"""
 :mod:`views` 
"""
from django.contrib.auth import authenticate
from django.views.generic.simple import direct_to_template


def home(request):
    """
    Default view for Colorado Springs Monthly Meeting Website
    """
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return direct_to_template(request,
                              'index.html',
                             {'user':user})
