__author__ = "Jeremy Nelson"


import datetime
import markdown
import os

from bs4 import BeautifulSoup
from collections import OrderedDict
from .settings import PROJECT_HOME

BUSINESS_MINUTE_FILENAME = 'MinutesForMeetingForWorshipForBusiness.md'

MINUTES_ROOT = os.path.split(PROJECT_HOME)[0]

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

def get_minute(year, month, minute='Business'):
    if minute == 'Business':
        file_path = os.path.join(MINUTES_ROOT,
                                 str(year),
                                 QUAKER_MONTHS.get(int(month)),
                                 BUSINESS_MINUTE_FILENAME)
    else:
        file_path = os.path.join(MINUTES_ROOT,
                                 str(year),
                                 QUAKER_MONTHS.get(int(month)),
                                 minute)
    if os.path.exists(file_path):
        meta_mrkdwn = markdown.Markdown(extensions=['meta'])
        with open(file_path) as fo:
            raw_mrkdwn = fo.read()
        mrkdwn_html = meta_mrkdwn.convert(raw_mrkdwn)
        return mrkdwn_html
                             

def get_minutes(year=None):
    """Helper function gets all the minutes for a year or all years if year
    is None"""
    minutes = []
    if year:
        for month in QUAKER_MONTHS.values():
            file_path = os.path.join(MINUTES_ROOT,
                                     str(year),
                                     month,
                                     BUSINESS_MINUTE_FILENAME)
            if os.path.exists(file_path):
                meta_mrkdwn = markdown.Markdown(extensions=['markdown.extensions.meta'])
                with open(file_path) as fo:
                    raw_mrkdwn = fo.read()
                mrkdwn_html = meta_mrkdwn.convert(raw_mrkdwn)
                md_date = datetime.datetime.strptime(
                    meta_mrkdwn.Meta.get('date')[0],
                    '%Y-%m-%dT%H:%M:%S')
                minutes.append({'date': md_date})
    else:
        for row in range(2011, datetime.datetime.now().year+1):
            minutes.extend(get_minutes(row))
    return minutes
    
    
