from django.contrib import admin

from alt_pages.models import DownloadFile, DownloadLog, Testimonial


class FileAdmin(admin.ModelAdmin):
    list_display = ('label', 'download_count', 'time_created')


class LogAdmin(admin.ModelAdmin):
    list_display = ('file', 'remote_ip', 'time_downloaded', 'user')
    list_filter = ('file', 'remote_ip', 'user')


admin.site.register(DownloadFile, FileAdmin)
admin.site.register(DownloadLog, LogAdmin)
admin.site.register(Testimonial)
