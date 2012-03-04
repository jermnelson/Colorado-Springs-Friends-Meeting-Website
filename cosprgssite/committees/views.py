"""
 :mod:views Colorado Springs Friends Meeting Committee View
"""
__author__ = "Jeremy Nelson"
import os,settings
from django.contrib.auth import authenticate
from django.http import HttpResponseNotFound
from django.views.generic.simple import direct_to_template
from committees.models import Committee,CommitteeMember,CommitteeReports,Position

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
          rst_file.close()
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
     committees = Committee.objects.filter(name=committee)
     if len(committees) < 1:
          return HttpResponseNotFound('<h2>%s Not Found</h2>' % committee)
     return direct_to_template(request,
                               'committee/detail.html',
                               {'committee':committees[0]})
                               
     

def display_monthly_report(request,
                           committee,
                           year,
                           month):
     """
     Function displays a reStructured Committee report

     :param year: YYYY four year digit string
     :param month: MM 01-12 digit 
     :param report_name: Name of rst report (filename)
     :rtype: Generated HTML
     """
     if request.user.is_authenticated():
          user = request.user
     else:
          user = None
     report_dir = os.path.join(settings.PROJECTBASE_DIR,
                               year,
                               month)
     report_path = "%/%s.rst" % (report_dir,report_name)
     if os.path.exists(report_path):
          # Should check datastore to see report protect,
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
