__author__ = "Jeremy Nelson"

from docutils.core import publish_string
from bs4 import BeautifulSoup
import os,sys,re
import json

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
year_loader = dict()
biz_re = re.compile(r"business")
finance_re = re.compile(r"finance")
mo_re = re.compiler(r"ministry")

def load(directory=CURRENT_DIR):
    month_walker = os.walk(directory)
    next(month_walker)
    for row in month_walker:
        path,filenames = row[0],row[2]
        month = os.path.split(path)[1]
        year_loader[month] = {"meetings":dict(),
                              "committees":dict()}
        for filename in filenames:
            raw_file = open(os.path.join(path,filename),'rb')
            raw_rst = raw_file.read()
            raw_file.close()
            rst_contents = publish_string(raw_rst,
                                          writer_name="html")
            rst_soup = BeautifulSoup(rst_contents)
            main_contents = rst_soup.find("div",attrs={"class":"document"})
            rst_category = guess_rst(filename)
            pretty_html = main_contents.prettify()
            if rst_category.has_key("meeting"):
                year_loader[month]['meetings'][rst_category.get("meeting")] = pretty_html
            if rst_category.has_key("committee"):
                year_loader[month]['committees'][rst_category.get("committee")] = pretty_html

    print("\t{0}".format(filename))

def guess_rst(filename):
    query = filename.lower()
    business_meeting_result = biz_re.search(query)
    if business_meeting_result is not None:
        return {"meeting":"business"}
    fiance_committee_result = finance_re.search(query)
    if fiance_committee_result is not None:
        return {"committee":"finance"}
    ministry_oversight_result = mo_re.search(query) 
    if ministry_oversight_result is not None:
        return {"committee":"ministry-and-oversight"}

load()
