from django.contrib import admin

from .models import FAQ, Application, ChatRequest, Course, Event, IndustryExpert, PhoneRequest, SkillCategory, Speaker, Testimonial, CourseEnquiry


@admin.register(IndustryExpert)
class IndustryExpertAdmin(admin.ModelAdmin):
    list_display = ("name", "priority", "logo")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "skill_category")
    search_fields = ("title",)
    ordering = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "designation")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question",)
    search_fields = ("question",)
    ordering = ("question",)


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ("name", "designation")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "time")
    search_fields = ("title",)
    ordering = ("title",)


@admin.register(PhoneRequest)
class PhoneRequestAdmin(admin.ModelAdmin):
    list_display = ("phone", "created_at")
    search_fields = ("phone",)
    ordering = ("-created_at",)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email", "phone")
    ordering = ("-created_at",)


@admin.register(ChatRequest)
class ChatRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email", "phone")
    ordering = ("-created_at",)


@admin.register(CourseEnquiry)
class CourseEnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "course", "created_at")
    search_fields = ("name", "email", "phone", "course")
    ordering = ("-created_at",)
