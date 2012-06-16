__author__ = "Jeremy Nelson"

from django.forms import *

class PersonForm(Form):
    address = CharField()
    city = CharField()
    confirm_email = CharField()
    email = CharField()
    first_name = CharField()
    last_name = CharField()
    message = CharField()
    organization = CharField(required=False)
    phone = CharField()
    state = CharField()
    zip_code = CharField()

