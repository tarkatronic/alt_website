from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site as filebrowser_site


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alt_website.views.home', name='home'),
    # url(r'^alt_website/', include('alt_website.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include(filebrowser_site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^subscribe/$', 'alt_pages.views.list_subscribe',
        name='mailchimp_subscribe'),
    url(r'^contact/$', 'alt_pages.views.contact', name='contact'),
    url(r'^download/(?P<file_id>\d+)/$', 'alt_pages.views.download',
        name='download_file'),
    url(r'^blog/', include('alt_blog.urls', namespace='alt_blog',
                           app_name='blog')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
