from main.mixins import HybridCreateView, HybridDeleteView, HybridDetailView, HybridListView, HybridUpdateView

from .mixins import HybridTemplateView
from .models import Standard, Student, Subject, Teacher
from .tables import StandardTable, StudentTable, SubjectTable, TeacherTable


class DashboardView(HybridTemplateView):
    template_name = "app/main/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StandardListView(HybridListView):
    model = Standard
    filterset_fields = ("name", "code")
    table_class = StandardTable
    search_fields = ("name", "code")


class StandardCreateView(HybridCreateView):
    model = Standard


class StandardDetailView(HybridDetailView):
    model = Standard


class StandardUpdateView(HybridUpdateView):
    model = Standard


class StandardDeleteView(HybridDeleteView):
    model = Standard


class SubjectListView(HybridListView):
    model = Subject
    filterset_fields = ("name", "code")
    table_class = SubjectTable
    search_fields = ("name", "code")


class SubjectCreateView(HybridCreateView):
    model = Subject


class SubjectDetailView(HybridDetailView):
    model = Subject


class SubjectUpdateView(HybridUpdateView):
    model = Subject


class SubjectDeleteView(HybridDeleteView):
    model = Subject


class TeacherListView(HybridListView):
    model = Teacher
    filterset_fields = ("user",)
    table_class = TeacherTable
    search_fields = ("user",)


class TeacherCreateView(HybridCreateView):
    model = Teacher


class TeacherDetailView(HybridDetailView):
    model = Teacher


class TeacherUpdateView(HybridUpdateView):
    model = Teacher


class TeacherDeleteView(HybridDeleteView):
    model = Teacher


class StudentListView(HybridListView):
    model = Student
    filterset_fields = ("user", "standard")
    table_class = StudentTable
    search_fields = ("user", "standard")


class StudentCreateView(HybridCreateView):
    model = Student


class StudentDetailView(HybridDetailView):
    model = Student


class StudentUpdateView(HybridUpdateView):
    model = Student


class StudentDeleteView(HybridDeleteView):
    model = Student
