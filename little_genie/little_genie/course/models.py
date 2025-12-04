import uuid

from django.db import models
from django.urls import reverse_lazy
from versatileimagefield.fields import VersatileImageField


class Course(models.Model):
    CATEGORY_CHOICE = (("Academic", "Academic"), ("Non-Academic", "Non-Academic"))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    category = models.CharField(max_length=250, choices=CATEGORY_CHOICE)
    title = models.CharField(max_length=250)
    image = VersatileImageField("Image", upload_to="images/course")
    description = models.TextField()
    course_duration = models.CharField(max_length=250)
    course_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse_lazy("course:view_course", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("course:update_course", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("course:delete_course", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


class CourseEnquiry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    child_name = models.CharField(max_length=250)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    is_checked = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.child_name)

    def get_absolute_url(self):
        return reverse_lazy("course:view_course_enquiry", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("course:update_course_enquiry", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("course:delete_course_enquiry", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]
