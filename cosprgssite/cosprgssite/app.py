__author__ = "Jeremy Nelson"

import datetime
import markdown
import os
import sys

from collections import OrderedDict
from flask import abort, Flask, render_template
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__)).split("cosprgssite")[0]

BUSINESS_MINUTE_FILENAME = 'MinutesForMeetingForWorshipForBusiness.md'

QUAKER_MONTHS= OrderedDict({1: 'first-month',
                            2: 'second-month',
                            3: 'third-month',
                            4: 'fourth-month',
                            5: 'fifth-month',
                            6: 'sixth-month',
                            7: 'seventh-month',
                            8: 'eighth-month',
                            9: 'ninth-month',
                            10: 'tenth-month',
                            11: 'eleventh-month',
                            12: 'twelfth-month'})


def get_minutes(year=None):
    """Helper function gets all the minutes for a year or all years if year
    is None"""
    def __get_year_minutes__(year):
        year_mins = []
        for month in QUAKER_MONTHS.values():
            file_path = os.path.join(PROJECT_ROOT,
                str(year),
                month,
                BUSINESS_MINUTE_FILENAME)
            if os.path.exists(file_path):
                meta_mrkdwn = markdown.Markdown(
                    extensions=['markdown.extensions.meta'])
                with open(file_path) as fo:
                    raw_mrkdwn = fo.read()
                mrkdwn_html = meta_mrkdwn.convert(raw_mrkdwn)
                md_date = datetime.datetime.strptime(
		            meta_mrkdwn.Meta.get('date')[0],
               '%Y-%m-%dT%H:%M:%S')
                year_mins.append(md_date)
        return year_mins
    minutes = []
    if year:
        minutes.extend(__get_year_minutes__(year))
    else:
        for row in range(2011, datetime.datetime.now().year+1):
            minutes.extend(__get_year_minutes__(row))
    mins = {}
    for i, row in enumerate(minutes):
        if i > 0 or i <= len(minutes):
            current_year = row.year
            if current_year == minutes[i-1].year and\
               current_year in mins:
                mins[current_year].append(row)
            else:
                 mins[current_year] = [row,]
    output = OrderedDict()
    for year in sorted(mins, reverse=True):
        output[year] = mins[year]
    return output

def _get_minute(year, month):
    year, month = int(year), int(month)
    if year < 2011 or month > 12 or month < 1:
        abort(404)
    file_path = os.path.join(
        PROJECT_ROOT,
        str(year),
        QUAKER_MONTHS.get(month),
        BUSINESS_MINUTE_FILENAME)
    if os.path.exists(file_path):
        meta_mrkdwn = markdown.Markdown(extensions=['meta'])
        with open(file_path) as fo:
            raw_mrkdwn = fo.read()
        mrkdwn_html = meta_mrkdwn.convert(raw_mrkdwn)
        return mrkdwn_html
    return abort(404)

@app.route("/committees/<path:name>")
@app.route("/committees")
def committee_route(name=None):
    if name is None:
        return render_template("committee-base.html")
    try:
        if name.endswith("/"):
            name = name[:-1]
        return render_template("{}.html".format(name.lower()),
						section="committee")
    except TemplateNotFound:
        abort(404)

@app.route("/Friends/<name>")
def friend_display(name):
    abort(401)

@app.route("/history/<path:topic>")
@app.route("/history")
def history_route(topic=None):
    if topic is not None:
        if topic.endswith("/"):
            topic = topic[:-1]
        try:
            return render_template("{}.html".format(topic))
        except TemplateNotFound:
            pass
    abort(404)

@app.route("/meetings/<name>/<year>/<path:month>")
@app.route("/meetings/<name>/<path:year>")
@app.route("/meetings/<path:name>")
@app.route("/meetings")
def meetings(name=None, year=None, month=None):
    if name.lower().startswith("worship"):
        return render_template("worship.html")
    if name and year and month:
        return render_template(
            'minute.html',
            category = 'about',
            content = _get_minute(year, month),
            section = 'meeting')
    return render_template("business.html",
        minutes=get_minutes(year),
        section="meeting")

@app.route("/testimonies/<name>")
@app.route("/testimonies")
def testimony(name=None):
    if name is None:
        return render_template(
            "testimonies.html",
			category='about',
			section='testimonies')
    return render_template(
        '{0}.html'.format(name.lower()),
        category='about',
        section='testimonies')

@app.route("/<path:page>")
@app.route("/")
def index(page=None):
    category=None
    if page is None:
        template_name = "index.html"
        category = 'home'
    else:
        if page.endswith("/"):
            page = page[:-1]
        template_name = "{}.html".format(page)
    try:
        return render_template(
            template_name,
            category=category)
    except TemplateNotFound:
        abort(404)



