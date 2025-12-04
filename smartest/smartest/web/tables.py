from main.base import BaseTable

from .models import ClassTest


class ClassTestTable(BaseTable):
    class Meta:
        model = ClassTest
        fields = ("test_id", "title", "due_date", "test_duration", "total_marks", "created_by")
        attrs = {"class": "table key-buttons border-bottom table-hover"}  # noqa: RUF012
