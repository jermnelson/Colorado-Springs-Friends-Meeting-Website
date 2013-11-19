__name__ = "Jeremy Nelson"

from django.forms import ModelForm
from friends.models import Friend, PostalAddress

class FriendForm(ModelForm):

    class Meta:
        model = Friend
        fields = ['birthday',
                  'category',
                  'is_birthright',
                  'is_public']


class PostalAddressForm(ModelForm):

    class Meta:
        model = PostalAddress
        fields = ['addressLocality',
                  'addressRegion',
                  'postalCode',
                  'streetAddress']
