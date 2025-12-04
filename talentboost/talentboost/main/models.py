from uuid import uuid4

from django.db import models
from django.urls import reverse

from .base import BaseModel


class School(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, blank=True)
    name = models.CharField("School Name", max_length=200)
    place = models.CharField("Place", max_length=200)
    district = models.CharField("District", max_length=200)
    pin_code = models.CharField("Pin code", max_length=200)
    poc_name = models.CharField("POC Name", max_length=200)
    contact_number = models.CharField("Contact Number", max_length=200)
    email_id = models.EmailField("Email ID")
    screenshot = models.FileField("Screenshot", upload_to="screenshots/")

    def get_absolute_url(self):
        return reverse("main:school_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse("main:school_list")

    # @staticmethod
    # def get_create_url():
    #     return reverse("main:school_create")

    # def get_update_url(self):
    #     return reverse("main:school_update", kwargs={"pk": self.pk})

    # def get_delete_url(self):
    #     return reverse("main:school_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class StudentRegistration(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, blank=True)
    name = models.CharField("Student Name", max_length=200)
    student_class = models.CharField("Class", max_length=200)
    syllabus = models.CharField("Syllabus", max_length=200)
    school_name = models.CharField("School Name", max_length=200)
    school_place = models.CharField("School Place", max_length=200)
    parent_name = models.CharField("Parent Name", max_length=200)
    place = models.CharField("Place", max_length=200)
    pin_code = models.CharField("Pin code", max_length=200)
    district = models.CharField("District", max_length=200)
    contact_number = models.CharField("Contact Number", max_length=200)
    whatsapp_number = models.CharField("WhatsApp Number", max_length=200)
    email_id = models.EmailField("Email ID")
    preferred_language = models.CharField("Preferred Language", max_length=200)
    preferred_exam_centre = models.CharField("Preferred Exam Centre", max_length=200)

    register_number = models.CharField("Register Number", max_length=200, blank=True, null=True, unique=True)
    coupon = models.CharField("Coupon (optional)", max_length=200, blank=True, null=True)
    razorpay_order_id = models.CharField("Razorpay Order ID", max_length=40, null=True, blank=True)
    razorpay_payment_id = models.CharField("Razorpay Payment ID", max_length=36, null=True, blank=True)
    razorpay_signature = models.CharField("Razorpay Signature ID", max_length=128, null=True, blank=True)
    is_paid = models.BooleanField("Is Paid", default=False)
    is_message_sent = models.BooleanField("Is Message Sent", default=False)
    paid_at = models.DateTimeField(blank=True, null=True)
    is_imported = models.BooleanField("Is Imported", default=False)

    def get_absolute_url(self):
        return reverse("main:student_registration_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse("main:student_registration_list")

    # @staticmethod
    # def get_create_url():
    #     return reverse("main:student_registration_create")

    def get_update_url(self):
        return reverse("main:student_registration_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("main:student_registration_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Document(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    file = models.FileField("Document", upload_to="mydocs/")

    @property
    def filename(self):
        name = self.file.name.split("/")[1].replace("_", " ").replace("-", " ")
        return name


class Coupon(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, blank=True)
    name = models.CharField("Coupon Name", max_length=200)
    code = models.CharField("Coupon Code", max_length=200, unique=True)
    discount = models.FloatField("Discount")
    is_active = models.BooleanField("Is Active", default=True)

    def get_absolute_url(self):
        return reverse("main:coupon_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse("main:coupon_list")

    @staticmethod
    def get_create_url():
        return reverse("main:coupon_create")

    def get_update_url(self):
        return reverse("main:coupon_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("main:coupon_delete", kwargs={"pk": self.pk})

    def used_count(self):
        return StudentRegistration.objects.filter(coupon=self.code).count()

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ImportedData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, blank=True)
    data = models.JSONField("Data")
    success_data = models.JSONField("Success Data", blank=True, null=True)
    failed_data = models.JSONField("Failed Data", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_imported = models.BooleanField("Is Imported", default=False)
    imported_count = models.IntegerField("Imported Count", blank=True, null=True)
    failed_count = models.IntegerField("Failed Count", blank=True, null=True)
    time_taken = models.DurationField("Time Taken", blank=True, null=True)

    def __str__(self):
        return str(self.id)
