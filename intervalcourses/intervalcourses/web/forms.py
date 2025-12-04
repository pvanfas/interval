from django import forms

from .models import FDEnquiry, LGEnquiry


class FDEnquiryIntroForm(forms.ModelForm):
    intro_phone_number_country_code = forms.CharField(max_length=5,required=False,widget=forms.HiddenInput(attrs={"id": "id_intro_phone_number_country_code"}))
    intro_whatsapp_number_country_code = forms.CharField(max_length=5,required=False,widget=forms.HiddenInput(attrs={"id": "id_intro_whatsapp_number_country_code"}))

    class Meta:
        model = FDEnquiry
        exclude = ("timestamp", "attempt", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your Name"}),
            "country": forms.Select(attrs={"placeholder": "Select Your Country"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Your Phone Number", "id": "id_intro_phone_number"}),
            "whatsapp_number": forms.TextInput(attrs={"placeholder": "Your WhatsApp Number","id": "id_intro_whatsapp_number"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter Your Email"}),
            "utm_source": forms.HiddenInput(),
            "utm_medium": forms.HiddenInput(),
            "utm_campaign": forms.HiddenInput(),
            "utm_content": forms.HiddenInput(),
            "utm_term": forms.HiddenInput(),
        }


class LGEnquiryForm(forms.ModelForm):
    intro_phone_number_country_code = forms.CharField(max_length=5, required=False, widget=forms.HiddenInput(attrs={"id": "id_intro_phone_number_country_code"}))
    intro_whatsapp_number_country_code = forms.CharField(max_length=5, required=False, widget=forms.HiddenInput(attrs={"id": "id_intro_whatsapp_number_country_code"}))

    class Meta:
        model = LGEnquiry
        exclude = ("timestamp", "attempt", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your Name"}),
            "country": forms.Select(attrs={"placeholder": "Select Your Country"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Your Phone Number", "id": "id_intro_phone_number"}),
            "whatsapp_number": forms.TextInput(attrs={"placeholder": "Your WhatsApp Number", "id": "id_intro_whatsapp_number"}),
            "age": forms.NumberInput(attrs={"placeholder": "Your Age"}),
            "utm_source": forms.HiddenInput(),
            "utm_medium": forms.HiddenInput(),
            "utm_campaign": forms.HiddenInput(),
            "utm_content": forms.HiddenInput(),
            "utm_term": forms.HiddenInput(),
        }
