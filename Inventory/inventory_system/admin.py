from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from inventory_system.models import desktops, headphones, laptops, smartphones

admin.site.site_header = 'Site Administration panel'
admin.site.site_title = 'Site Administration panel'
admin.site.index_title = 'Site Administration Panel'

@admin.register(laptops, smartphones, desktops, headphones)
class ViewAdmin(ImportExportModelAdmin):
    pass
