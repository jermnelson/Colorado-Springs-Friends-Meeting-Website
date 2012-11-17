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
    address = CharField()
    amount = CharField()
    city = CharField()
    confirm_email = CharField()
    email = CharField()
    first_name = CharField()
    last_name = CharField()
    message = CharField()
    organization = CharField(required=False)
    payment_frequency = ChoiceField(choices=FREQUENCY)
    payment_options = ChoiceField(widget=RadioSelect(),
                                  choices=PAYMENT_OPTIONS)
    phone = CharField()
    state = CharField()
    zip_code = CharField()

