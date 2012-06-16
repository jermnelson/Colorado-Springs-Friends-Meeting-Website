__author__ = "Jeremy Nelson"
import json,sys
from Friends.models import *
from location.models import Address
from django.contrib.auth.models import User
import settings
from docutils.core import publish_string
from bs4 import BeautifulSoup
import os,sys,re
biz_re = re.compile(r"business")
finance_re = re.compile(r"finance")
mo_re = re.compile(r"ministry")


def associate_addresses(addresses_filename):
    print("Associate addresses with Friends")
    addr_json = json.load(open(addresses_filename,'r'))
    for row in addr_json:
        addr_query = Address.objects.filter(md5_key=row["addr"])
        addr = addr_query[0]
        friends = get_friends(row["friends"])
        for friend in friends:
            friend.address = addr
            friend.save()
            print("\t%s address set to %s, %s" % (friend.short_name,
                                                  addr.street,
                                                  addr.city))
    print("Finished associating addresses with Friends")


def associate_categories(categories_filename):
    print("Associate categories with Friends")
    categories_json = json.load(open(categories_filename,'r'))
    for row in categories_json:
        new_category = FriendCategory(code=row["code"],
                                      label=row["label"])
        new_category.save()
        new_category.friends = get_friends(row["friends"])
        new_category.save()
    print("Finished associating categories")

def build_loader(year_loader,directory):
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
    return year_loader
    
def get_friends(friend_keys):
    friends = []
    for friend_key in friend_keys:
        friend_query = Friend.objects.filter(md5_key=friend_key)
        friends.append(friend_query[0])
    return friends

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
    return {}



def load_base(ADDR_JSON,CATEGORY_JSON):
    associate_addresses(ADDR_JSON)
    associate_categories(CATEGORY_JSON)
    # Sets admin to correct values
    jeremy = User.objects.get(pk=1)
    jeremy.first_name = 'Jeremy'
    jeremy.last_name = 'Nelson'
    jeremy.save()

def load_windows():
    ADDR_JSON = 'H:\\jermsmemory\\ColoradoSpringsMeeting\\2012\\friend-addresses.json'
    CATEGORY_JSON = 'H:\\jermsmemory\\ColoradoSpringsMeeting\\2012\\friend-categories.json'
    load_base(ADDR_JSON,CATEGORY_JSON)

def load_linux():
    ADDR_JSON = '/home/jpnelson/jermsmemory/ColoradoSpringsMeeting/2012/friend-addresses.json'
    CATEGORY_JSON = '/home/jpnelson/jermsmemory/ColoradoSpringsMeeting/2012/friend-categories.json'
    load_base(ADDR_JSON,CATEGORY_JSON)

year2011 = build_loader(dict(),os.path.join(settings.PROJECTBASE_DIR,'2011')) 
year2012 = build_loader(dict(),os.path.join(settings.PROJECTBASE_DIR,'2012'))



if __name__ == '__main__':
    pass
