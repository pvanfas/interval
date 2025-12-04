from uuid import uuid4

from django.db import models
from django_tables2 import Table, columns
from import_export.admin import ImportExportActionModelAdmin

from users.models import CustomUser as User

from .actions import mark_active, mark_inactive
from .choices import BOOL_CHOICES
from .functions import generate_fields


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, blank=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, editable=False, blank=True, null=True, related_name="%(app_label)s_%(class)s_creator", on_delete=models.PROTECT)
    is_active = models.BooleanField("Mark as Active", default=True, choices=BOOL_CHOICES)

    class Meta:
        abstract = True
        ordering = ("-created_at",)

    def get_fields(self):
        return generate_fields(self)


class BaseAdmin(ImportExportActionModelAdmin):
    exclude = ("creator", "is_active")
    list_display = ("__str__", "created_at", "updated_at", "is_active")
    list_filter = ("is_active",)
    actions = (mark_active, mark_inactive)
    readonly_fields = ("is_active", "creator", "pk")
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
