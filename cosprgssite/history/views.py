__author__ = "Jeremy Nelson"

from django.http import HttpResponse

def default(request):
    return HttpResponse("NEEDS CONTENT -- History Index Page")

def emancipation_and_suffrage(request):
    return HttpResponse("NEEDS CONTENT -- Emancipation and Suffrage")

def hicksite(request):
    return HttpResponse("NEEDS CONTENT -- Hicksite Split")

def religious_society_of_friends(request):
    return HttpResponse("NEEDS CONTENT -- Religious Society Of Friends")


