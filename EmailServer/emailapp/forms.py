from django import forms
from emailapp.models import EMailCompose


class EmailForm(forms.ModelForm):
    class Meta:
        model = EMailCompose
        fields = ['email','cc','bcc','subject','message','attach']








"""
class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    attach = forms.Field(widget=forms.FileInput)

"""