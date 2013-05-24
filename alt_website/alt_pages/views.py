from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from mailchimp import utils

from alt_pages.forms import MailChimpForm


@require_POST
def list_subscribe(request):
    form = MailChimpForm(data=request.POST)
    if form.is_valid():
        chimp_list = utils.get_connection().get_list_by_id(
                                                   settings.MAILCHIMP_LIST_ID)
        email = form.cleaned_data['email']
        name = form.cleaned_data['name']
        if ' ' in name:
            (fname, lname) = name.split(' ', 1)
        else:
            fname = name
            lname = ''
        chimp_list.subscribe(email, {'EMAIL': email, 'FNAME': fname,
                                     'LNAME': lname})
        if request.is_ajax():
            return HttpResponse(status=200)
        else:
            messages.success(request, 'You have been subscribe to the mailing '
                             'list.')
            return HttpResponseRedirect('/')
    else:
        if request.is_ajax():
            return HttpResponse(status=400)
        else:
            messages.error(request, 'Please fill in your name and a valid '
                           'email address.')
            return HttpResponseRedirect('/')
