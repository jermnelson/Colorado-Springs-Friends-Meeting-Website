__author__ = 'Jeremy Nelson'

from django.template import Context,Library,loader
from django.utils.safestring import mark_safe
from Friends.models import PhoneNumber

register = Library()

def census_display(friend):
    phone_query = PhoneNumber.objects.filter(friends=friend.pk)
    params = {'friend':friend,
              'phone_numbers':phone_query}
    census_detail_template = loader.get_template('Friends/snippets/census-detail.html')
    census_html = census_detail_template.render(Context(params))
    return mark_safe(census_html)


register.filter('census_display',census_display)
    
