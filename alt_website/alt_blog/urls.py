from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.views.generic.dates import DateMixin

from alt_blog.models import Post


class BlogPostView(DetailView, DateMixin):
    pass

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Post)),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[0-9a-zA-Z-_]+)/$',
        BlogPostView.as_view(model=Post, date_field='time_posted'),
        name='view_post')
)
