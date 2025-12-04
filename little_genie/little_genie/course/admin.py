from course.models import Course
from course.models import CourseEnquiry
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Course)
class CourseAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "category", "course_duration", "course_duration")


@admin.register(CourseEnquiry)
class CourseEnquiryAdmin(ImportExportActionModelAdmin):
    list_display = ("child_name", "email", "phone", "course", "message", "timestamp")
