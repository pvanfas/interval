from core.models import FAQ
from core.models import About
from core.models import Contact
from core.models import Feature
from core.models import Gallery
from core.models import Social
from core.models import Testimonial
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Testimonial)
class TestimonialAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "description")


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Contact)
class ContactAdmin(ImportExportActionModelAdmin):
    list_display = ("child_name", "email", "phone", "message", "timestamp")


@admin.register(Feature)
class FeatureAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "image")


@admin.register(Social)
class SocialAdmin(ImportExportActionModelAdmin):
    list_display = ("link", "is_active")


@admin.register(FAQ)
class FAQAdmin(ImportExportActionModelAdmin):
    list_display = ("question", "answer")
