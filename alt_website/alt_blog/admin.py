from django.conf import settings
from django.contrib import admin

from alt_blog.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'site')
    list_filter = ('site', 'author')
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = ('%sgrappelli/tinymce/jscripts/tiny_mce/tiny_mce.js' %
              settings.STATIC_URL,
              '%sjs/tinymce_setup.js' %
              settings.STATIC_URL)

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
