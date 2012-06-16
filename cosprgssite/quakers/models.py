from django.db import models


class EmailLog(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    return_email = models.EmailField(blank=True,null=True)
