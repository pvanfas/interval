from django.db import models
from django_tables2 import Table, columns
from import_export.admin import ImportExportModelAdmin

from .actions import mark_active, mark_inactive
from .functions import generate_fields


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_at",)

    def get_fields(self):
        return generate_fields(self)


class BaseAdmin(ImportExportModelAdmin):
    exclude = ("creator",)
    list_display = ("__str__", "created_at", "updated_at")
    actions = (mark_active, mark_inactive)
    readonly_fields = ("creator", "pk")
    search_fields = ("pk",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creator = request.user
        super().save_model(request, obj, form, change)

    class Media:
        css = {"all": ("extra_admin/css/admin.css",)}


class BaseTable(Table):
    pk = columns.Column(visible=False)
    action = columns.TemplateColumn(template_name="app/partials/table_actions.html", orderable=False)
