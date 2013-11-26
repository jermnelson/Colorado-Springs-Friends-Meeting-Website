__name__ = "Jeremy Nelson"

from django.forms import ModelForm
from django.forms.models import modelformset_factory
from friends.models import Friend, PostalAddress, PhoneNumber

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

class TelephoneForm(ModelForm):

    class Meta:
        model = PhoneNumber
        fields = ['number',
                  'phone_number_type']

TelephoneFormSet = modelformset_factory(PhoneNumber,
                                        fields=['number',
                                                'phone_number_type'])
