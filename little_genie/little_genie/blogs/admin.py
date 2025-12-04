from django.contrib import admin

from .models import Author
from .models import Blog


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "email")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "published_time", "is_featured")
