__author__ = "Jeremy Nelson"

from django.contrib.auth.models import Group, User
from friends.models import Category, Friend, PostalAddress, PhoneNumber

CATEGORIES = {}
for row in Category.objects.all():
    CATEGORIES[row.code] = row

def get_or_load_address(info):
    postal_address = None
    if not 'PostalAddress' in  info:
        return postal_address
    results = PostalAddress.objects.all().filter(
        streetAddress=info['PostalAddress'].get('streetAddress'))
    if len(results) > 0:
        postal_address = results[0]
    else:
        postal_address = PostalAddress()
        for key, value in info['PostalAddress'].iteritems():
            setattr(postal_address,
                    key,
                    value)
        postal_address.save()
    return postal_address
            

def load_friend(info):
    address = get_or_load_address(info)
    new_user = User(username=info.get('csq:username'),
                    first_name=info.get('givenName'),
                    last_name=info.get('familyName'))
    if info.has_key('email'):
        new_email.email = info.get('email')
    new_email.save()
    new_friend = Friend(category=category.get(
        info.get('csq:category').get('csq:code').lower()),
                        postal_address=address,
                        user=new_user)
    new_friend.save()
    
                        
