"""
 :mod:views Colorado Springs Friends Meeting Committee View
"""
__author__ = "Jeremy Nelson"

import os,settings,logging
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound,HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from committees.models import *
from committees.forms import *

committee_templates = {'Education':'committees/education.html',
                       'Finance':'committees/finance.html',
                       'MeetingHouse':'committees/meeting-house.html',
                       'MinistryAndOversight':'committees/ministry-and-oversight.html',
                       'Nominating':'committees/nominating.html',
                       'REA':'committees/rea.html',
                       'ReligiousEducationAndAction':'committees/rea.html'}
                       

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
     user,forms = None,None
     if request.user.is_authenticated():
          user = request.user
          if user.is_superuser:
               committees = Committee.objects.all()
               forms = {'committee_form':CommitteeForm(),
                        'members_form':CommitteeMemberForm(),
                        'report_form':CommitteeReportForm(),
                        'committees':committees}
     return direct_to_template(request,
                               'committees/index.html',
                               {'forms':forms,
                                'user':user})


def display_committee(request,
                      committee):
     """
     Function displays a detail view for a single committee

     :param committee: Name of committee
     """
     committees_query = Committee.objects.filter(name=committee)
     members_form,report_form = None,None
     if len(committees_query) > 0:
          committee_info = committees_query[0]
          member_query = CommitteeMember.objects.filter(committee=committee_info)
          committee_info = committee_info
          members = member_query
          current_reports = CommitteeReport.objects.filter(committee=committee_info)
          if request.user.is_superuser:
               members_form = CommitteeMemberForm(instance=committee_info)
               report_form = CommitteeReportForm(instance=committee_info)
     else:
          committee_info = {'name':committee}
          members,current_reports = [],[]
          if request.user.is_superuser:
               members_form = CommitteeMemberForm()
               report_form = CommitteeReportForm()
          
##   
##     if len(committees) < 1:
##          return HttpResponseNotFound('<h2>%s Not Found</h2>' % committee)
     return direct_to_template(request,
                               committee_templates[committee],
                               {'committee':committee_info,
                                'committee_members':members,
                                'members_form':members_form,
                                'reports':current_reports,
                                'report_form':report_form})
                               
     

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
     report_type = None
     for row in REPORT_TYPES:
          if row[1] == report_name:
               report_type = row[0]
     reports = CommitteeReport.objects.filter(committee=committee_obj,report_type=report_type)
     if len(reports) > 0:
          # Should check datastore to see report permissions
          report = reports[0]
          relative_path = os.path.join(year,
                                       QUAKER_MONTHS[month],
                                       report.rstFileLocation)
          report_path = "%s/%s" % (settings.PROJECTBASE_DIR,
                                  relative_path)
          report_rst = get_report(os.path.normpath(report_path))
     else:
          report = {'report_type':-1,
                    'report_date':datetime.date(year=year,month=month,day=1),
                    'contents':report_rst}
          report_rst = '''Report %s does not exist''' % report_name
     return direct_to_template(request,
                               'committees/report.html',
                               {'user':user,
                                'report':report,
                                'contents':report_rst})

def save_committee(request):
     if request.user.is_superuser and request.method == 'POST':
          if request.POST.has_key('existing-committee'):
               committee = Committee.objects.get(pk=request.POST['existing-committee'])
               new_name = request.POST.get('name')
               committee.name = new_name
               committee.save()
          else:
               committee_form = CommitteeForm(request.POST)
               committee = committee_form.save()
     return HttpResponseRedirect('/committees/')

def add_member(request,committee):
     if request.user.is_superuser and request.method == 'POST':
          committee_obj = Committee.objects.filter(name=committee)[0]
          friend = User.objects.get(pk=request.POST.get('user'))
          new_member = CommitteeMember(committee=committee_obj,
                                       user=friend,
                                       date_joined=request.POST.get('date_joined'))
          new_member.save()
     return HttpResponseRedirect('/committees/%s/' % committee)
     
def add_report(request,committee):
    """
    Add report view 

    :param committee: Committee name 
    """
    if request.user.is_superuser and request.method == 'POST':
        committee_obj = Committee.objects.filter(name=committee)[0]
        authors = request.POST.get('authors')
        report_type = request.POST.get('report_type')
        report_date = request.POST.get('report_date')
        file_location = request.POST.get('rstFileLocation')
        new_report = CommitteeReport(committee=committee_obj,
                                     report_date=report_date,
                                     report_type=report_type,
                                     rstFileLocation=file_location)
        new_report.save()
    return HttpResponseRedirect('/committees/%s/' % committee)
       
                             
          
               
     
     

def display_yearly_report(request,committee,year):
    return direct_to_template(request,
                              'committees/report.html',
                              {'user':None,
                               'report':{'name':'%s Yearly Report %s' % (year,committee),
                                         'contents':'Yearly Report Contents'}})
