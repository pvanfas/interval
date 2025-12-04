import datetime
import json
import time

import simplejson
import tablib
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from main.mixins import HybridCreateView, HybridDeleteView, HybridDetailView, HybridFormView, HybridListView, HybridUpdateView, HybridView
from web.views import generate_register_number

from .filters import StudentRegistrationFilter
from .forms import ImportForm
from .mixins import HybridTemplateView
from .models import Coupon, Document, ImportedData, School, StudentRegistration
from .tables import CouponTable, DocumentTable, SchoolTable, StudentRegistrationTable
from .utils import send_bulk_whatsapp_message, send_whatsapp_message


class DashboardView(HybridTemplateView):
    template_name = "app/main/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["student_count"] = StudentRegistration.objects.count()
        context["school_count"] = School.objects.count()
        return context


class CouponListView(HybridListView):
    model = Coupon
    filterset_fields = ("name", "code", "discount", "is_active")
    table_class = CouponTable
    search_fields = ("name", "is_active")


class CouponCreateView(HybridCreateView):
    model = Coupon


class CouponDetailView(HybridDetailView):
    model = Coupon


class CouponUpdateView(HybridUpdateView):
    model = Coupon


class CouponDeleteView(HybridDeleteView):
    model = Coupon


class DocumentListView(HybridListView):
    model = Document
    filterset_fields = ("name", "file")
    table_class = DocumentTable
    search_fields = ("name",)


class DocumentCreateView(HybridCreateView):
    model = Document


class DocumentDetailView(HybridDetailView):
    model = Document


class DocumentUpdateView(HybridUpdateView):
    model = Document


class DocumentDeleteView(HybridDeleteView):
    model = Document


class SchoolListView(HybridListView):
    model = School
    filterset_fields = ("district",)
    table_class = SchoolTable
    search_fields = ("name", "place", "district", "pin_code", "poc_name")


class SchoolCreateView(HybridCreateView):
    model = School


class SchoolDetailView(HybridDetailView):
    model = School


class SchoolUpdateView(HybridUpdateView):
    model = School


class SchoolDeleteView(HybridDeleteView):
    model = School


class StudentRegistrationListView(HybridListView):
    model = StudentRegistration
    filterset_class = StudentRegistrationFilter
    table_class = StudentRegistrationTable
    search_fields = ("name", "student_class", "syllabus", "place", "pin_code", "coupon")


class StudentRegistrationCreateView(HybridCreateView):
    model = StudentRegistration


class StudentRegistrationDetailView(HybridDetailView):
    model = StudentRegistration


class StudentRegistrationResendView(HybridDetailView):
    model = StudentRegistration
    template_name = "app/main/student_registration_resend.html"

    def post(self, request, *args, **kwargs):
        student = self.get_object()
        send_whatsapp_message(student)
        return redirect("main:student_registration_list")


class StudentRegistrationUpdateView(HybridUpdateView):
    model = StudentRegistration
    exclude = ("coupon", "register_number", "razorpay_order_id", "razorpay_payment_id", "razorpay_signature", "is_paid", "is_message_sent", "paid_at", "is_imported")


class StudentRegistrationDeleteView(HybridDeleteView):
    model = StudentRegistration


class ManageImportView(HybridFormView):
    template_name = "app/main/manage_import.html"
    form_class = ImportForm
    success_url = reverse_lazy("main:manage_import")

    def form_valid(self, form):
        file = form.cleaned_data["file"]
        dataset = tablib.Dataset().load(file.read())
        data_list = dataset.dict
        filtered_data = [row for row in data_list if any(value not in [None, "", "null"] for value in row.values())]
        data_json = simplejson.dumps(filtered_data)
        item = ImportedData.objects.create(data=data_json)
        return redirect("main:complete_import", pk=item.pk)


class CompleteImportView(HybridView):
    template_name = "app/main/complete_import.html"

    def get(self, request, *args, **kwargs):
        item = ImportedData.objects.get(pk=self.kwargs["pk"])
        return render(request, self.template_name, {"item": item})

    def post(self, request, *args, **kwargs):
        item = get_object_or_404(ImportedData, pk=self.kwargs["pk"])
        data = json.loads(item.data)
        success_data = []
        failed_data = []
        initial_time = time.time()
        imported_count = 0
        failed_count = 0

        for row in data:
            try:
                student = StudentRegistration.objects.create(
                    name=str(row.get("name")),
                    student_class=str(row.get("student_class")),
                    syllabus=str(row.get("syllabus")),
                    school_name=str(row.get("school_name")),
                    school_place=str(row.get("school_place")),
                    parent_name=str(row.get("parent_name")),
                    place=str(row.get("place")),
                    pin_code=str(row.get("pin_code")),
                    district=str(row.get("district")),
                    contact_number=str(row.get("contact_number")),
                    whatsapp_number=str(row.get("whatsapp_number")),
                    email_id=str(row.get("email_id")),
                    preferred_language=str(row.get("preferred_language")),
                    preferred_exam_centre=str(row.get("preferred_exam_centre")),
                    coupon=str(row.get("coupon")),
                )
                student.register_number = generate_register_number(student)
                student.is_imported = True
                student.save()
                imported_count += 1
                success_data.append(str(student.pk))
                print(f"Successfully created student: {student.name}")
            except Exception as e:
                print(f"Error: {e}")
                failed_data.append(row)
                failed_count += 1
        item.is_imported = True
        item.imported_count = imported_count
        item.failed_count = failed_count
        item.success_data = json.dumps(success_data)
        item.failed_data = json.dumps(failed_data)
        item.time_taken = datetime.timedelta(seconds=(time.time() - initial_time))
        item.save()
        return redirect("main:status_import", pk=item.pk)


class StatusImportView(HybridDetailView):
    model = ImportedData
    template_name = "app/main/status_import.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.get_object()
        students_pks = json.loads(item.success_data)
        students = StudentRegistration.objects.filter(pk__in=students_pks)
        message_sent_count = students.filter(is_message_sent=True).count()
        context["message_sent_count"] = message_sent_count
        context["total_count"] = students.count()
        context["sent_percent"] = (message_sent_count / students.count()) * 100
        return context

    def post(self, request, *args, **kwargs):
        item = self.get_object()
        send_bulk_whatsapp_message(item)
        return redirect("main:status_import", pk=item.pk)
