__author__ = "Jeremy Nelson"
from django.shortcuts import render_to_response

def home(request):
    return render_to_response(
        'index.html')
        

    
