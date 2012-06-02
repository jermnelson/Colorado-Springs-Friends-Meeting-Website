__author__ = "Jeremy Nelson"

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.generic.simple import direct_to_template

from django.http import HttpResponse
from history.doc import json_loader,rst_loader
from fixures import json_loader as fixures_json

history_info = fixures_json.get('history-info')

def default(request):
    return direct_to_template(request,
                              'history/index.html',
                              {'section':'history'})


def abolition_and_suffrage(request):
    topic = history_info[3]
    docs = [ rst_loader.get(topic.get('rst')),]
    return direct_to_template(request,
                              'history/topic.html',
                              {'docs':docs,
                               'next': history_info[4],
                               'section':'history',
                               'topic':topic,
                               'user':None})
    

def colorado_springs(request):
    topic = history_info[5]
    docs = [ rst_loader.get(topic.get('rst')),]
    return direct_to_template(request,
                              'history/topic.html',
                              {'docs':docs,
                               'next': None,
                               'section':'history',
                               'topic':topic,
                               'user':None})

def george_fox_first_quakers(request):
    topic = history_info[0]
    docs = [ rst_loader.get(topic.get('rst')),]
    return direct_to_template(request,
                              'history/topic.html',
                              {'docs':docs,
                               'next':history_info[1],
                               'section':'history',
                               'topic':topic,
                               'user':None})

def hicksite(request):
    topic = history_info[2]
    docs = [ rst_loader.get(topic.get('rst')),]
    return direct_to_template(request,
                              'history/topic.html',
                              {'docs':docs,
                               'next': history_info[3],
                               'section':'history',
                               'topic':topic,
                               'user':None})

def religious_society_of_friends(request):
    topic = history_info[1]
    docs = [ rst_loader.get(topic.get('rst')),]
    return direct_to_template(request,
                              'history/topic.html',
                              {'docs':docs,
                               'next': history_info[2],
                               'section':'history',
                               'topic':topic,
                               'user':None})

def worldwars_conscientious_objectors(request):
    topic = history_info[4]
    docs = [ rst_loader.get(topic.get('rst')),]
    return direct_to_template(request,
                              'history/topic.html',
                              {'docs':docs,
                               'next': history_info[5],
                               'section':'history',
                               'topic':topic,
                               'user':None})

