from models import EmailLog
from django.forms import *

class EmailContactForm(ModelForm):

    class Meta:
        model=EmailLog
