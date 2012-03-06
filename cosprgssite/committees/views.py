"""
 :mod:views Colorado Springs Friends Meeting Committee View
"""
__author__ = "Jeremy Nelson"

import os,settings,logging
from django.contrib.auth import authenticate
from django.http import HttpResponseNotFound
from django.views.generic.simple import direct_to_template
from committees.models import Committee,CommitteeMember,CommitteeReport,Position

committee_templates = {'Education':'committees/education.html',
                       'Finance':'committees/finance.html',
                       'Meeting House':'committees/meeting-house.html',
                       'MinistryAndOversight':'committees/ministry-and-oversight.html',
                       'Nominating':'committees/nominating.html',
                       'Religious Education and Action':'rea.html'}
                       

def get_report(rst_path):
     """
     Returns the reStructured text

     :param rst_path: Path including file name of committee rst
     """
     try:
          rst_file = open(rst_path,'rb')
          rst_contents = rst_file.read()
          rst_file.close()
     except:
          raise
          #rst_file.close()
     return rst_contents
     

def default(request):
     """
     Displays Committees of Meeting and Related organizations
     """
     if request.user.is_authenticated():
          user = request.user
     else:
          user = None
     return direct_to_template(request,
                               'committees/index.html',
                               {'user':user})


def display_committee(request,
                      committee):
     """
     Function displays a detail view for a single committee

     :param committee: Name of committee
     """
     committees_query = Committee.objects.filter(name=committee)
     if len(committees_query) > 0:
          committee_info = committees_query[0]
          member_query = CommitteeMember.objects.filter(committee=committee_info)
          committee_info = committee_info
          members = member_query
          current_reports = CommitteeReport.objects.filter(committee=committee_info)     
     else:
          committee_info = {'name':committee}
          members,current_reports = [],[]
##   
##     if len(committees) < 1:
##          return HttpResponseNotFound('<h2>%s Not Found</h2>' % committee)
     return direct_to_template(request,
                               committee_templates[committee],
                               {'committee':committee_info,
                                'committee_members':members,
                                'reports':current_reports})
                               
     

def display_monthly_report(request,
                           committee,
                           year,
                           month,
                           report_name):
     """
     Function displays a reStructured Committee report

     :param committee: Name of committee
     :param year: YYYY four year digit string
     :param month: MM 01-12 digit 
     :param report_name: Name of rst report (filename)
     :rtype: Generated HTML
     """
     if request.user.is_authenticated():
          user = request.user
     else:
          user = None
     committee_query = Committee.objects.filter(name=committee)
     committee_obj = committee_query[0]
     reports = CommitteeReport.objects.filter(committee=committee_obj,name=report_name)
     if len(reports) > 0:
          # Should check datastore to see report protect,
          report_path = os.path.join(settings.PROJECTBASE_DIR,
                                     reports[0].rstFileLocation)
          logging.error("REPORT path is %s" % settings.PROJECTBASE_DIR)
          report_rst = get_report(report_path)
     else:
          report_rst = '''Report %s does not exist''' % report_name
     return direct_to_template(request,
                               'committees/report.html',
                               {'user':user,
                                'report':{'name':report_name,
                                          'contents':report_rst}})

def display_yearly_report(request,committee,year):
    return direct_to_template(request,
                              'committees/report.html',
                              {'user':None,
                               'report':{'name':'%s Yearly Report %s' % (year,committee),
                                         'contents':'Yearly Report Contents'}})
