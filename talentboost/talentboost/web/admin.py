from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import FAQ, Achievement, Feature, News, Project, Setting, Winner


@admin.register(Achievement)
class AchievementAdmin(ImportExportActionModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(News)
class NewsAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "content")
    search_fields = ("title", "content")


@admin.register(Project)
class ProjectAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "content")
    search_fields = ("title", "content")


@admin.register(Feature)
class FeatureAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "content")
    search_fields = ("title", "content")


@admin.register(Winner)
class WinnerAdmin(ImportExportActionModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(FAQ)
class FAQAdmin(ImportExportActionModelAdmin):
    list_display = ("question",)
    search_fields = ("question",)


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    pass

    def has_add_permission(self, request):
        return Setting.objects.count() == 0
