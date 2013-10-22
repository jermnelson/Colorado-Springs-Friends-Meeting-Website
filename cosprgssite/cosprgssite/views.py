__author__ = "Jeremy Nelson"
from django.shortcuts import render

def home(request):
    return render(request,
                  'index.html')
        

    
