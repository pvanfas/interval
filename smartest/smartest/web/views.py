from django.shortcuts import render
from django.views.generic import TemplateView

from main.mixins import HybridCreateView, HybridDeleteView, HybridDetailView, HybridListView, HybridUpdateView
from main.utils import send_welcome_email

from .models import ClassTest
from .tables import ClassTestTable


class HomeView(TemplateView):
    template_name = "app/home.html"


def test(request):
    send_welcome_email("anfaspv.info@gmail.com")
    return render(request, "test.html")


class ClassTestListView(HybridListView):
    model = ClassTest
    filterset_fields = ("test_id", "title")
    table_class = ClassTestTable
    search_fields = ("test_id", "title")


class ClassTestCreateView(HybridCreateView):
    model = ClassTest


class ClassTestDetailView(HybridDetailView):
    model = ClassTest


class ClassTestUpdateView(HybridUpdateView):
    model = ClassTest


class ClassTestDeleteView(HybridDeleteView):
    model = ClassTest
