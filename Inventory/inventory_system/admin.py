from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from inventory_system.models import desktops, headphones, laptops, smartphones


@admin.register(laptops, smartphones, desktops, headphones)
class ViewAdmin(ImportExportModelAdmin):
    pass
