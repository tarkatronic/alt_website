import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    site = models.ForeignKey('sites.Site')
    title = models.CharField(max_length=500)
    slug = models.SlugField()
    author = models.ForeignKey('auth.User')
    time_posted = models.DateTimeField(default=datetime.datetime.now())
    content = models.TextField()
    header_image = models.ImageField(upload_to='alt_blog/headers',
                                     null=True, blank=True)
    categories = models.ManyToManyField('alt_blog.Category',
                                        related_name='posts', null=True,
                                        blank=True)

    class Meta:
        ordering = ['-time_posted']

    def __unicode__(self):
        return self.title
