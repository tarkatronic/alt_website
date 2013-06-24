from django.db import models
from django.utils.translation import ugettext_lazy as _


class DownloadFile(models.Model):
    file = models.FileField(upload_to='alt_pages/downloads')
    time_created = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey('auth.User', null=True, blank=True)

    def __unicode__(self):
        return self.label

    def download_count(self):
        return self.downloads.all().count()


class DownloadLog(models.Model):
    file = models.ForeignKey(DownloadFile, related_name='downloads')
    remote_ip = models.IPAddressField()
    time_downloaded = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', null=True, blank=True)


class Testimonial(models.Model):
    cited = models.CharField(_('cited person'), max_length=255,
                             help_text=_('Who is this testimonial quoting?'))
    quote = models.TextField(_('quote'))
    testimonial_date = models.DateField()

    def __unicode__(self):
        return u'%s (%s-%s-%s)' % (self.cited, self.testimonial_date.year,
                                   self.testimonial_date.month,
                                   self.testimonial_date.day)
