from django import forms
from django.contrib.localflavor.us import forms as us_forms
from django.utils.translation import ugettext_lazy as _


class MailChimpForm(forms.Form):
    name = forms.CharField(label=_('name'), max_length=255, required=True)
    email = forms.EmailField(label=_('email'), max_length=255, required=True)


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=255, required=True)
    email = forms.EmailField(label=_('Email'), max_length=255, required=False)
    phone = us_forms.USPhoneNumberField(label=_('Phone #'), required=False)
    comments = forms.CharField(label=_('Comments'), required=True,
                               widget=forms.Textarea)

    def clean(self):
        email = self.cleaned_data.get('email', '').strip()
        phone = self.cleaned_data.get('phone', '').strip()
        if not any([email, phone]):
            raise forms.ValidationError('You must provide either an email '
                                        'address or phone number.')
