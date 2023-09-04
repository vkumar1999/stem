from django.contrib import admin
from import_export.admin import ImportExportMixin
# Register your models here.
from .models import contactform
class contactformAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']
admin.site.register(contactform,contactformAdmin)