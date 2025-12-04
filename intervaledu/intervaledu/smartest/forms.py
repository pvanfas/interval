from django import forms

from .models import TestLink


class TestLinkForm(forms.ModelForm):
    class Meta:
        model = TestLink
        exclude = ("link",)
