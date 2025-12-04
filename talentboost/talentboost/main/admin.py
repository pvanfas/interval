from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import Coupon, Document, ImportedData, School, StudentRegistration


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 0


@admin.register(School)
class SchoolAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "contact_number", "district")
    search_fields = ("name", "contact_number", "district")
    inlines = [DocumentInline]


@admin.register(StudentRegistration)
class StudentRegistrationAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "register_number", "created_at", "district", "pin_code", "coupon", "is_paid", "is_message_sent", "paid_at", "is_imported")
    search_fields = ("name", "syllabus")
    list_filter = ("is_paid", "is_message_sent", "is_imported")


@admin.register(Document)
class DocumentAdmin(ImportExportActionModelAdmin):
    list_display = ("school", "filename", "created_at")
    search_fields = ("school", "file")


@admin.register(Coupon)
class CouponAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "code", "discount", "used_count", "is_active")
    search_fields = ("name", "code", "discount", "is_active")


@admin.register(ImportedData)
class ImportedDataAdmin(ImportExportActionModelAdmin):
    pass
