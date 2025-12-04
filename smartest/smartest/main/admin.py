from django.contrib import admin

from main.base import BaseAdmin

from .models import Notification, Standard, Student, Subject, Syllabus, Teacher


@admin.register(Subject)
class SubjectAdmin(BaseAdmin):
    list_display = ("__str__", "code", "syllabus", "is_active")
    search_fields = ("name",)
    list_filter = ("standard", "syllabus")


@admin.register(Standard)
class StandardAdmin(BaseAdmin):
    list_display = ("__str__", "is_active")
    search_fields = ("name",)


@admin.register(Teacher)
class TeacherAdmin(BaseAdmin):
    list_display = ("user", "subjects_list", "is_active")
    autocomplete_fields = ("subjects", "user")
    search_fields = ("user__first_name", "user__last_name")


@admin.register(Student)
class StudentAdmin(BaseAdmin):
    list_display = ("user", "student_id", "standard", "is_active")
    autocomplete_fields = ("standard", "user")
    search_fields = ("user__first_name", "user__last_name", "student_id")


@admin.register(Notification)
class NotificationAdmin(BaseAdmin):
    list_display = ("title", "message", "is_active")
    search_fields = ("title", "message")
    list_filter = ("is_active",)
    autocomplete_fields = ("user",)


@admin.register(Syllabus)
class SyllabusAdmin(BaseAdmin):
    list_display = ("name", "is_active")
