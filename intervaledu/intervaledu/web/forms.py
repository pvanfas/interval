from django import forms

from .models import ContactData, DemoRequest, Enquiry, Payment


class ContactDataForm(forms.ModelForm):
    phone_number_country_code = forms.CharField(max_length=5, required=False, widget=forms.HiddenInput())
    whatsapp_number_country_code = forms.CharField(max_length=5, required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["purpose"].empty_label = "-- Select Purpose --"

    class Meta:
        model = ContactData
        exclude = ("timestamp", "attempt", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your Name"}),
            "country": forms.Select(attrs={"placeholder": "Select Your Country"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Your Phone Number"}),
            "whatsapp_number": forms.TextInput(attrs={"placeholder": "Your WhatsApp Number"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter Your Email"}),
            "purpose": forms.Select(attrs={"placeholder": "Select Purpose"}),
            "utm_source": forms.HiddenInput(),
            "utm_medium": forms.HiddenInput(),
            "utm_campaign": forms.HiddenInput(),
            "utm_content": forms.HiddenInput(),
            "utm_term": forms.HiddenInput(),
        }


class EnquiryPopupForm(forms.ModelForm):
    popup_phone_number_country_code = forms.CharField(
        max_length=5,
        required=False,
        widget=forms.HiddenInput(attrs={"id": "id_popup_phone_number_country_code"}),
    )
    popup_whatsapp_number_country_code = forms.CharField(
        max_length=5,
        required=False,
        widget=forms.HiddenInput(attrs={"id": "id_popup_whatsapp_number_country_code"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["purpose"].empty_label = "-- Select Purpose --"

    class Meta:
        model = Enquiry
        exclude = ("timestamp", "attempt", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your Name"}),
            "country": forms.Select(attrs={"placeholder": "Select Your Country"}),
            "phone_number": forms.TextInput(
                attrs={
                    "placeholder": "Your Phone Number",
                    "id": "id_popup_phone_number",
                }
            ),
            "whatsapp_number": forms.TextInput(
                attrs={
                    "placeholder": "Your WhatsApp Number",
                    "id": "id_popup_whatsapp_number",
                }
            ),
            "email": forms.EmailInput(attrs={"placeholder": "Enter Your Email"}),
            "purpose": forms.Select(attrs={"placeholder": "Select Purpose"}),
            "utm_source": forms.HiddenInput(),
            "utm_medium": forms.HiddenInput(),
            "utm_campaign": forms.HiddenInput(),
            "utm_content": forms.HiddenInput(),
            "utm_term": forms.HiddenInput(),
        }


class DemoRequestForm(forms.ModelForm):
    demo_phone_number_country_code = forms.CharField(max_length=5, required=False, widget=forms.HiddenInput())
    demo_whatsapp_number_country_code = forms.CharField(max_length=5, required=False, widget=forms.HiddenInput())

    class Meta:
        model = DemoRequest
        exclude = ("timestamp", "status", "attempt")
        widgets = {
            "student_name": forms.TextInput(),
            "email": forms.EmailInput(),
            "country": forms.Select(),
            "phone_number": forms.TextInput(attrs={"id": "id_demo_phone_number"}),
            "whatsapp_number": forms.TextInput(attrs={"id": "id_demo_whatsapp_number"}),
            "standard": forms.Select(),
            "utm_source": forms.HiddenInput(),
            "utm_medium": forms.HiddenInput(),
            "utm_campaign": forms.HiddenInput(),
            "utm_content": forms.HiddenInput(),
            "utm_term": forms.HiddenInput(),
        }


class PaymentForm(forms.ModelForm):
    phone_number_country_code = forms.CharField(max_length=5, required=False, widget=forms.HiddenInput())
    whatsapp_number_country_code = forms.CharField(max_length=5, required=False, widget=forms.HiddenInput())

    class Meta:
        model = Payment
        exclude = ("timestamp", "status", "discount_amount")
        widgets = {
            "student_name": forms.TextInput(),
            "email": forms.EmailInput(),
            "country": forms.Select(),
            "phone_number": forms.TextInput(),
            "whatsapp_number": forms.TextInput(),
            "standard": forms.Select(),
            "referred_by": forms.TextInput(),
        }
