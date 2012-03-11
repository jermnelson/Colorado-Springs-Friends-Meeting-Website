__author__ = "Jeremy Nelson"

from django.http import HttpResponse

def default(request):
    return HttpResponse("NEEDS CONTENT -- History Index Page")

def abolition_and_suffrage(request):
    return HttpResponse("NEEDS CONTENT -- Abolition and Suffrage")

def colorado_springs(request):
    return HttpResponse("NEEDS CONTENT -- Local Quaker history in Colorado Springs")

def hicksite(request):
    return HttpResponse("NEEDS CONTENT -- Hicksite Split")

def religious_society_of_friends(request):
    return HttpResponse("NEEDS CONTENT -- Religious Society Of Friends")

def worldwars_conscientious_objectors(request):
    return HttpResponse("NEEDS CONTENT -- World Wars and Conscientious Objectors")


