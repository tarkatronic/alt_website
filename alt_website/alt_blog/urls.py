from django.conf.urls import patterns, url
from django.views.generic import ListView

from alt_blog.models import Post


urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Post))
)
