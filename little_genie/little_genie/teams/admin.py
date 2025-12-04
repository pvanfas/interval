from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from teams.models import Team


@admin.register(Team)
class TeamAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "designation")
