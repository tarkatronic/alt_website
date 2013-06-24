import mimetypes
import os

from django.conf import settings
from django.contrib import messages
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from mailchimp import utils

from alt_pages.forms import MailChimpForm
from alt_pages.models import DownloadFile, DownloadLog


@require_POST
def list_subscribe(request):
    form = MailChimpForm(data=request.POST)
    next_page = request.POST.get('next', '/')
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
            messages.success(request, 'You have been sent a confirmation email. '
                             'Please follow the instructions within to confirm '
                             'your subscription.')
            return HttpResponseRedirect(next_page)
    else:
        if request.is_ajax():
            return HttpResponse(status=400)
        else:
            messages.error(request, 'Please fill in your name and a valid '
                           'email address.')
            return HttpResponseRedirect(next_page)


def download(request, file_id):
    dl = get_object_or_404(DownloadFile, id=file_id)
    user = request.user.is_authenticated() and request.user or None
    log = DownloadLog(file=dl, remote_ip=request.META['REMOTE_ADDR'],
                      time_downloaded=timezone.now(), user=user)
    log.save()
    mt = mimetypes.guess_type(os.path.basename(dl.file.path))[0]
    wrapper = FileWrapper(dl.file)
    response = HttpResponse(wrapper, content_type=mt)
    response['Content-Disposition'] = ('attachment; filename=%s' %
                                       os.path.split(dl.file.name)[1])
    response['Content-Length'] = os.path.getsize(dl.file.path)
    return response
