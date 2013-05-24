from django import forms
from django.utils.translation import ugettext_lazy as _


class MailChimpForm(forms.Form):
    name = forms.CharField(label=_('name'), max_length=255, required=True)
    email = forms.EmailField(label=_('email'), max_length=255, required=True)
