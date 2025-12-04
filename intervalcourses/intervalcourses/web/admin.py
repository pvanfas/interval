from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import FDEnquiry, Slider, Testimonial, Configuration, LGEnquiry


@admin.register(Slider)
class SliderAdmin(ImportExportActionModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Testimonial)
class TestimonialAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "designation")
    search_fields = ("name", "designation")


@admin.register(FDEnquiry)
class FDEnquiryAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "phone_number", "whatsapp_number", "timestamp", "lsq_status_code")
    search_fields = ("name", "phone_number", "whatsapp_number")
    list_filter = ("lsq_status_code", "lsq_status", "lsq_exception_type", "lsq_exception_message")


@admin.register(LGEnquiry)
class LGEnquiryAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "phone_number", "whatsapp_number", "timestamp")
    search_fields = ("name", "phone_number", "whatsapp_number")
    

@admin.register(Configuration)
class ConfigurationAdmin(ImportExportActionModelAdmin):
    list_display = ("key", "value")
    search_fields = ("key", "value")
