__author__ = "Jeremy Nelson"

import datetime
import markdown
import os

from meetings import MINUTES_ROOT, QUAKER_MONTHS

COMMITTEE_REPORT_NAMES = {
    'Finance': 'FinanceReport.md',
    'MeetingHouse': 'MeetingHouseReport.md',
    'MinistryAndOversight':'MinistryAndOversightReport.md',
    'Nominating': 'NominatingReport.md'}
