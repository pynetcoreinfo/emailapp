from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from django.core.mail import send_mail,EmailMessage

class EMailCompose(models.Model):
    email = models.EmailField()
    cc = models.EmailField(default="")
    bcc = models.EmailField(default="")
    subject = models.CharField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    date_sented = models.DateTimeField(null=True,blank=True)
    attach = models.FileField(upload_to='email_file',default='default.csv')
    message = models.TextField()

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('mail-detail', kwargs={'pk': self.pk})



"""
class EmailInfo(models.Model):
    subject = models.CharField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='date_sented')
    date_sented = models.DateTimeField()
    message = models.TextField()
"""