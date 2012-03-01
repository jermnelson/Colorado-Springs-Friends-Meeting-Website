"""
 :mod:`views` 
"""
from django.views.generic.simple import direct_to_template


def home(request):
    """
    Default view for Colorado Springs Monthly Meeting Website
    """
    user = None
    return direct_to_template(request,
                              'index.html',
                             {'user':user})
