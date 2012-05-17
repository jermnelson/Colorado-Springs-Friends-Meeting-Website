__author__ = "Jeremy Nelson"
import json,sys
from Friends.models import *

def associate_json():
    pass

def associate_categories(categories_filename):
    print("Associate categories with Friends")
    categories_json = json.load(categories_filename)
    for row in categories_json:
        new_category = FriendCategory(code=row["code"],
                                      label=row["label"])
        new_category.save()
        friends = []
        for friend_key in row["friends"]:
            friend_query = Friend.objects.filter(md5_key=friend_key)
            friends.append(friend_query[0])
            print("\t%s category is %s" % (friend_query[0].short_name,
                                           new_category.label))
        new_category.friends = friends
        new_category.save()
    print("Finished associating categories")
