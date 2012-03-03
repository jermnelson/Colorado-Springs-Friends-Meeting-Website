"""
 :mod:views Colorado Springs Friends Meeting Committee View
"""
__author__ = "Jeremy Nelson"
import os,settings
from django.contrib.auth import authenticate
from django.views.generic.simple import direct_to_template


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
     Displays for committees of Meeting and Related organizations
     """
     if request.user.is_authenticated():
          user = request.user
     else:
          user = None
     return direct_to_template(request,
                               'committees/index.html',
                               {'user':user})

def display_report(request,
                   year,
                   month,
                   day,
                   report_name):
     """
     Function displays a reStructured Committee report

     :param year: YYYY four year digit string
     :param month: MM 01-12 digit 
     :param day: DD 01-31 digit
     :param report_name: Name of rst report (filename)
     :rtype: Generated HTML
     """
     if request.user.is_authenticated():
          user = request.user
     else:
          user = None
     report_dir = os.path.join(settings.PROJECTBASE_DIR,
                               year,
                               month,
                               day)
     report_path = "%/%s" % (report_dir,report_name)
     if os.path.exists(report_path):
          # Should check datastore to see report protect,
          report_rst = get_report(report_path)
     else:
          report_rst = '''Report %s does not exist''' % report_name
     return direct_to_template(request,
                               'committees/report.html',
                               {'user':user,
                                'report_rst':report_rst})
