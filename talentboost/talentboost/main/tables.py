from django_tables2 import columns

from main.base import BaseTable

from .models import Coupon, Document, School, StudentRegistration


class CouponTable(BaseTable):
    class Meta:
        model = Coupon
        fields = ("name", "code", "discount", "used_count", "is_active")
        attrs = {"class": "table key-buttons border-bottom table-hover"}  # noqa: RUF012


class DocumentTable(BaseTable):
    class Meta:
        model = Document
        fields = ("name", "file", "is_active")
        attrs = {"class": "table key-buttons border-bottom table-hover"}  # noqa: RUF012


class SchoolTable(BaseTable):
    files = columns.TemplateColumn(
        """
        <div class="d-flex">
        {% for file in record.document_set.all %}
            <a href="{{ file.file.url }}" target="_blank" class="dwdicon" title="{{file.file}}"><img src="/static/app/images/svgs/download.svg" style="height:10px;"/></a>
        {% endfor %}
        </div>
        """,
        verbose_name="Files",
    )

    class Meta:
        model = School
        fields = ("name", "place", "district", "pin_code", "poc_name")
        attrs = {"class": "table key-buttons border-bottom table-hover"}  # noqa: RUF012


class StudentRegistrationTable(BaseTable):
    action = columns.TemplateColumn(template_name="app/partials/student_table_actions.html", orderable=False)
    coupon = columns.Column(accessor="coupon", orderable=True, verbose_name="Coupon")

    class Meta:
        model = StudentRegistration
        fields = ("register_number", "name", "student_class", "syllabus", "district", "coupon", "is_paid", "is_message_sent", "is_imported")
        attrs = {"class": "table key-buttons border-bottom table-hover"}  # noqa: RUF012
