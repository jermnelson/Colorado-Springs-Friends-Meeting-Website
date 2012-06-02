"""
 :mod:`event_extras` - Template Tags for managing basic events and display calendar in
 a template. Original source at http://djangosnippets.org/snippets/2464/
"""
from calendar import HTMLCalendar
from django import template
from datetime import date
from itertools import groupby

from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape as esc

from events.models import CommitteeEvent,Event,MeetingEvent
from bs4 import BeautifulSoup

register = template.Library()
##
##def do_event_calendar(parser, token):
##    """
##    The template tag's syntax is {% event_calendar year month event_list %}
##    """
##
##    try:
##        tag_name, year, month, event_list = token.split_contents()
##    except ValueError:
##        raise template.TemplateSyntaxError, "%r tag requires three arguments" % token.contents.split()[0]
##    return EventCalendarNode(year, month, event_list)
##
##
##class EventCalendarNode(template.Node):
##    """
##    Process a particular node in the template. Fail silently.
##    """
##
##    def __init__(self, year, month, event_list):
##        try:
##            self.year = template.Variable(year)
##            self.month = template.Variable(month)
##            self.event_list = template.Variable(event_list)
##        except ValueError:
##            raise template.TemplateSyntaxError
##
##    def render(self, context):
##        try:
##            # Get the variables from the context so the method is thread-safe.
##            my_event_list = self.event_list.resolve(context)
##            my_year = self.year.resolve(context)
##            my_month = self.month.resolve(context)
##            cal = EventCalendar(my_event_list)
##            return cal.formatmonth(int(my_year), int(my_month))
##        except ValueError:
##            return          
##        except template.VariableDoesNotExist:
##            return
##
##
##class EventCalendar(HTMLCalendar):
##    """
##    Overload Python's calendar.HTMLCalendar to add the appropriate events to
##    each day's table cell.
##    """
##
##    def __init__(self, events):
##        super(EventCalendar, self).__init__()
##        self.events = self.group_by_day(events)
##
##    def formatday(self, day, weekday):
##        if day != 0:
##            cssclass = self.cssclasses[weekday]
##            if date.today() == date(self.year, self.month, day):
##                cssclass += ' today'
##            if day in self.events:
##                cssclass += ' filled'
##                body = ['<ul>']
##                for event in self.events[day]:
##                    body.append('<li>')
##                    body.append('<a href="%s">' % event.get_absolute_url())
##                    body.append(esc(event.series.primary_name))
##                    body.append('</a></li>')
##                body.append('</ul>')
##                return self.day_cell(cssclass, '<span class="dayNumber">%d</span> %s' % (day, ''.join(body)))
##            return self.day_cell(cssclass, '<span class="dayNumberNoEvents">%d</span>' % (day))
##        return self.day_cell('noday', '&nbsp;')
##
##    def formatmonth(self, year, month):
##        self.year, self.month = year, month
##        return super(EventCalendar, self).formatmonth(year, month)
##
##    def group_by_day(self, events):
##        field = lambda event: event.date_and_time.day
##        return dict(
##            [(day, list(items)) for day, items in groupby(events, field)]
##        )
##
##    def day_cell(self, cssclass, body):
##        return '<td class="%s">%s</td>' % (cssclass, body)


def current_calendar(default):
    current = date.today()
    html_calendar = HTMLCalendar()
    raw_html = html_calendar.formatmonth(current.year,
                                         current.month)
    calendar_soup = BeautifulSoup(raw_html)
    all_tds = calendar_soup.find_all("td")
    for td in all_tds:
        try:
            td_day = int(td.text)
            if td.attrs["class"] == current.strftime("%a").lower():
                if td_day == current.day:
                    td.attrs["class"].append("active")
            td_date = datetime.datetime(current.year,current.month,td_day)
            meeting_events = MeetingEvent.objects.filter(start_on >= td_date)
            if len(meeting_events) > 0:
                td.text = ""
                td_link = calendar_soup.tag("a",href="/events/%s/%s/%s" % (current.year,
                                                                             current.month,
                                                                             td_day))
                td_link.text = unicode(td_day)
                td.append(td_link)
        except:
            pass
    return mark_safe(calendar_soup)

##register.tag("event_calendar", do_event_calendar)
register.filter("get_calendar",current_calendar)
