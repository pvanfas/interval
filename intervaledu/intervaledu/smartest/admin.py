from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import Subject, TestLink


@admin.register(Subject)
class SubjectAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(TestLink)
class TestLinkAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "board", "standard", "subject", "link")
    list_filter = ("board", "standard", "subject")
    search_fields = ("board", "standard", "subject")
    autocomplete_fields = ("board", "subject")
