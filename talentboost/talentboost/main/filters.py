import django_filters

from .models import StudentRegistration


class StudentRegistrationFilter(django_filters.FilterSet):
    class Meta:
        model = StudentRegistration
        fields = {
            "syllabus": ["exact"],
            "coupon": ["exact"],
            "student_class": ["exact"],
            "preferred_language": ["exact"],
            "preferred_exam_centre": ["exact"],
            "is_paid": ["exact"],
            "is_imported": ["exact"],
            "created_at": ["date__gte", "date__lte"],
            "paid_at": ["date__gte", "date__lte"],
        }
