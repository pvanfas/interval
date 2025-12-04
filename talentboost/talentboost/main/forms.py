from django import forms
from django.forms import HiddenInput

from .choices import DISTRICT_CHOICES, EXAM_CENTRE_CHOICES, LANGUAGE_CHOICES, STANDARD_CHOICES, SYLLABUS_CHOICES
from .models import School, StudentRegistration


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        exclude = ["screenshot"]


class SchoolPaymentForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ["screenshot"]


class StudentRegistrationForm(forms.ModelForm):
    selected_contact_number_country_code = forms.CharField(widget=HiddenInput, required=False)
    selected_whatsapp_country_code = forms.CharField(widget=HiddenInput, required=False)
    preferred_exam_centre = forms.ChoiceField(choices=EXAM_CENTRE_CHOICES)
    district = forms.ChoiceField(choices=DISTRICT_CHOICES)
    preferred_language = forms.ChoiceField(choices=LANGUAGE_CHOICES)
    student_class = forms.ChoiceField(choices=STANDARD_CHOICES)
    syllabus = forms.ChoiceField(choices=SYLLABUS_CHOICES)

    class Meta:
        model = StudentRegistration
        fields = (
            "name",
            "student_class",
            "syllabus",
            "school_name",
            "school_place",
            "parent_name",
            "place",
            "pin_code",
            "district",
            "contact_number",
            "whatsapp_number",
            "email_id",
            "preferred_language",
            "preferred_exam_centre",
        )


class ImportForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={"accept": ".xlsx", "class": "form-control"}))
