from django import forms

from .models import Application, ChatRequest, PhoneRequest, CourseEnquiry


class PhoneRequestForm(forms.ModelForm):
    class Meta:
        model = PhoneRequest
        fields = ("phone",)
        widgets = {
            "phone": forms.TextInput(attrs={"placeholder": "Phone number"}),
        }


class ChatRequestForm(forms.ModelForm):
    class Meta:
        model = ChatRequest
        fields = ("name", "email", "phone", "city")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone number"}),
            "city": forms.TextInput(attrs={"placeholder": "City"}),
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("name", "email", "phone", "city", "interests")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone number"}),
            "city": forms.TextInput(attrs={"placeholder": "City"}),
            "interests": forms.Textarea(attrs={"placeholder": "Interests", "rows": 4}),
        }


class CourseEnquiryForm(forms.ModelForm):
    class Meta:
        model = CourseEnquiry
        fields = ("name", "email", "phone", "whatsapp", "message")
        widgets = {
            "name": forms.TextInput(attrs={}),
            "email": forms.EmailInput(attrs={}),
            "phone": forms.TextInput(attrs={}),
            "whatsapp": forms.TextInput(attrs={}),
            "message": forms.Textarea(attrs={"rows": 4}),
        }
