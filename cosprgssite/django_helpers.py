__author__ = "Jeremy Nelson"
import json,sys
from Friends.models import *
from location.models import Address


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

    
def get_friends(friend_keys):
    friends = []
    for friend_key in friend_keys:
        friend_query = Friend.objects.filter(md5_key=friend_key)
        friends.append(friend_query[0])
    return friends
