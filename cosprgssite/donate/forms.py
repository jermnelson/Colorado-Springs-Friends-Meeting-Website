__author__ = "Jeremy Nelson"

from django.forms import *
FREQUENCY = (('weekly','Weekly'),
             ('monthly','Monthly'),
             ('quarterly','Quarterly'),
             ('semi-annual','Semi-annual'),
             ('annual','Annual'))

PAYMENT_OPTIONS = (('onetime','One-time'),
                   ('recurring','Recurring'))

class PersonForm(Form):
    address = CharField(widget=Textarea(attrs={'rows':4, 'cols':60}))
    amount = CharField()
    city = CharField()
    confirm_email = CharField()
    country = CharField(required=False)
    email = CharField()
    first_name = CharField()
    last_name = CharField()
    message = CharField(required=False,
                        widget=Textarea(attrs={'rows':4, 'cols':60}))
    organization = CharField(required=False)
    payment_frequency = ChoiceField(choices=FREQUENCY)
    payment_options = ChoiceField(widget=RadioSelect(),
                                  choices=PAYMENT_OPTIONS)
    phone = CharField(required=False)
    state = CharField()
    zip_code = CharField()

