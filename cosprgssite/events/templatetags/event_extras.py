"""
 :mod:`event_extras` - Template Tags for managing basic events and display calendar in
 a template. Original source at http://djangosnippets.org/snippets/2464/
"""
from calendar import HTMLCalendar
from django import template
import datetime
from itertools import groupby
import sys
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape as esc
from django.utils.safestring import SafeUnicode
from events.models import CommitteeEvent,Event,MeetingEvent
from bs4 import BeautifulSoup

register = template.Library()


def current_calendar(default):
    if type(default) == SafeUnicode:
        current = datetime.datetime.today()
    else:
        current = default
    print(type(current))
    html_calendar = HTMLCalendar()
    raw_html = html_calendar.formatmonth(current.year,
                                         current.month)
    calendar_soup = BeautifulSoup(raw_html)
    all_tds = calendar_soup.find_all("td")
    for td in all_tds:
        try:
            td_day = int(td.text)
            if td.attrs["class"][0] == current.strftime("%a").lower():
                if td_day == current.day:
                    td.attrs["class"].append("active")
            td_date = datetime.datetime(current.year,current.month,td_day)
            meeting_events = MeetingEvent.objects.filter(
                                    start_on__year=td_date.year
                                ).filter(
                                    start_on__month=td_date.month
                                ).filter(
                                    start_on__day=td_date.day)
            if len(meeting_events) > 0:
                td.string = ""
                td_link_href = "/events/{:04}/{:02}/{:02}".format(current.year,
                                                               current.month,
                                                               td_day)
                td_link = calendar_soup.new_tag("a",href=td_link_href)
                td_link.string = unicode(td_day)
                td_link.attrs["data-original-title"] = "Events"
                td_link.attrs["rel"] = "popover"
                td_link.attrs["data-content"] = str()
                for event in meeting_events:
                     td_link.attrs["data-content"] += "<p>%s</p>" % event.name
                td.append(td_link)
        except:
            pass
    return mark_safe(calendar_soup)

register.filter("get_calendar",current_calendar)
