from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from main.base import BaseModel


class Standard(BaseModel):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = _("Standard")
        verbose_name_plural = _("Standards")

    def get_absolute_url(self):
        return reverse_lazy("main:standard_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("main:standard_list")

    @staticmethod
    def get_create_url():
        return reverse_lazy("main:standard_create")

    def get_update_url(self):
        return reverse_lazy("main:standard_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("main:standard_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)


class Subject(BaseModel):
    standard = models.ForeignKey("main.Standard", on_delete=models.CASCADE, related_name="subjects")
    syllabus = models.ForeignKey("main.Syllabus", on_delete=models.CASCADE, related_name="subjects")
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def get_students(self):
        return Student.objects.filter(standard=self.standard)

    def get_students_count(self):
        return self.get_students().count()

    def get_absolute_url(self):
        return reverse_lazy("main:subject_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("main:subject_list")

    @staticmethod
    def get_create_url():
        return reverse_lazy("main:subject_create")

    def get_update_url(self):
        return reverse_lazy("main:subject_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("main:subject_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.standard} - {self.name}"


class Teacher(BaseModel):
    user = models.OneToOneField("users.CustomUser", on_delete=models.CASCADE, limit_choices_to={"usertype": "Teacher"})
    subjects = models.ManyToManyField("main.Subject", related_name="teachers", blank=True)

    class Meta:
        ordering = ("user__first_name", "user__last_name")
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")

    def subjects_list(self):
        return ", ".join([str(subject) for subject in self.subjects.all()])

    def get_students(self):
        subjects = self.subjects.prefetch_related("standard")
        standards = subjects.values_list("standard", flat=True).distinct()
        return Student.objects.filter(standard__in=standards)

    def get_classes(self):
        return self.subjects.filter(is_active=True)

    def get_assignments(self):
        return self.assignment_created_by.filter(is_active=True)

    def get_class_tests(self):
        return self.class_test_created_by.filter(is_active=True)

    def get_practice_tests(self):
        return self.practice_test_created_by.filter(is_active=True)

    def get_mock_tests(self):
        return self.mock_test_created_by.filter(is_active=True)

    def get_total_classes(self):
        return self.subjects.count()

    def get_total_students(self):
        return self.get_students().count()

    def get_absolute_url(self):
        return reverse_lazy("main:teacher_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("main:teacher_list")

    @staticmethod
    def get_create_url():
        return reverse_lazy("main:teacher_create")

    def get_update_url(self):
        return reverse_lazy("main:teacher_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("main:teacher_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.user)


class Student(BaseModel):
    student_id = models.CharField(max_length=200, unique=False)
    user = models.OneToOneField("users.CustomUser", on_delete=models.CASCADE, limit_choices_to={"usertype": "Student"})
    standard = models.ForeignKey("main.Standard", on_delete=models.CASCADE, related_name="students", blank=True, null=True)

    class Meta:
        ordering = ("user__first_name", "user__last_name")
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def get_marks(self):
        assignments = self.assignment_submissions_student.filter(is_valuated=True)
        classtest_submissions = self.test_submissions_student.filter(is_valuated=True)
        return sum([submission.marks for submission in assignments]) + sum([submission.marks_obtained() for submission in classtest_submissions])

    def get_grade(self):
        assignment_submissions = self.assignment_submissions_student.filter(is_valuated=True)
        grant_assignment_marks = sum([sub.total_marks for sub in assignment_submissions])
        total_assignment_obtained = sum([sub.marks_obtained() for sub in assignment_submissions])

        classtest_submissions = self.test_submissions_student.filter(is_valuated=True)
        grant_test_marks = sum([sub.marks_obtained() for sub in classtest_submissions])
        total_test_marks = sum([sub.marks_obtained() for sub in classtest_submissions])

        grant_total_marks = grant_assignment_marks + grant_test_marks
        total_marks_obtained = total_assignment_obtained + total_test_marks
        if grant_total_marks == 0:
            return "-"  # Prevent division by zero
        percentage = (total_marks_obtained / grant_total_marks) * 100
        grade_thresholds = [(90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D"), (40, "E")]
        for threshold, grade in grade_thresholds:
            if percentage >= threshold:
                return grade
        return "F"

    def get_absolute_url(self):
        return reverse_lazy("main:student_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("main:student_list")

    @staticmethod
    def get_create_url():
        return reverse_lazy("main:student_create")

    def get_update_url(self):
        return reverse_lazy("main:student_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("main:student_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.user)


class Notification(BaseModel):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE, related_name="notifications")
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")

    def __str__(self):
        return str(self.message)


class Syllabus(BaseModel):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("Syllabus")
        verbose_name_plural = _("Syllabus")

    def __str__(self):
        return f"{self.name}"
