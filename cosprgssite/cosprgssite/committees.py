__author__ = "Jeremy Nelson"

import datetime
import markdown
import os

from meetings import MINUTES_ROOT as REPORTS_ROOT
from meetings import QUAKER_MONTHS

COMMITTEE_REPORT_NAMES = {
    'Finance': 'FinanceReport.md',
    'MeetingHouse': 'MeetingHouseReport.md',
    'MinistryAndOversight':'MinistryAndOversightReport.md',
    'Nominating': 'NominatingReport.md'}

def get_report_metadata(year,
                        month,
                        committee_name):
    """
    Returns metadata for a single report

    Parameters:
    year -- Year of report
    month -- Month of report
    committee_name -- Name of committee
    """
    file_path = os.path.join(REPORTS_ROOT,
                             str(year),
                             QUAKER_MONTHS.get(int(month)),
                             COMMITTEE_REPORT_NAMES.get(
                                 committee_name))
    if os.path.exists(file_path):
        meta_mrkdwn = markdown.Markdown(
            extensions=['meta'])
        raw_mrkdwn = open(file_path, 'rb').read()
        mrkdwn_html = meta_mrkdwn.convert(raw_mrkdwn)
        md_date = datetime.datetime.strptime(
            meta_mrkdwn.Meta.get('date')[0],
            '%Y-%m-%dT%H:%M:%S')
        return md_date
        

def get_reports(committee_name, year=None):
    """Helper function returns all reports either by year or if year is
    none, all years.

    Parameter:
    committee_name -- name of committee
    year --  Year of reports, default is None
    """
    reports = []
    if not committee_name in COMMITTEE_REPORT_NAMES:
        raise ValueError("{0} not found".format(
            committee_name))
    if year is not None:
        for month in QUAKER_MONTHS:
            report_date = get_report_metadata(
                str(year),
                month,
                committee_name)
            if report_date is not None:
                reports.append(report_date)
    else: # Retrieves all reports since 2011
        for year in range(2011, datetime.datetime.now().year+1):
            reports.extend(get_reports(
                committee_name,
                year))
    return reports
                
            
                
                                     
    
