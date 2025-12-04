from main.base import BaseTable

from .models import Standard, Student, Subject, Teacher


class StandardTable(BaseTable):
    class Meta:
        model = Standard
        fields = ("name", "code")
        attrs = {"class": "table key-buttons border-bottom table-hover"}  # noqa: RUF012


class SubjectTable(BaseTable):
    class Meta:
        model = Subject
        fields = ("name", "code")
        attrs = {"class": "table key-buttons border-bottom table-hover"}  # noqa: RUF012


class TeacherTable(BaseTable):
    class Meta:
        model = Teacher
        fields = ("user", "subjects")
        attrs = {"class": "table key-buttons border-bottom table-hover"}  # noqa: RUF012


class StudentTable(BaseTable):
    class Meta:
        model = Student
        fields = ("user", "standard")
        attrs = {"class": "table key-buttons border-bottom table-hover"}  # noqa: RUF012
