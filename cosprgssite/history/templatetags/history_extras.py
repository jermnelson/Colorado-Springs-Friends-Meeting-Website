__author__ = "Jeremy Nelson"

from django.template import Context,Library,loader
from django.utils.safestring import mark_safe

from fixures import json_loader

register = Library()

def generate_history_menu(section):
    history_topics = json_loader.get('history-info')
    output = ''
    for topic in history_topics:
        output += '\n<li><a href="%s">%s</a></li>' % (topic["url"],
                                                      topic["title"])
    return mark_safe(output)


register.filter('history_menu',generate_history_menu)
