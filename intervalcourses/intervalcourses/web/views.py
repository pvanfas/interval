from django.shortcuts import render
from django.utils.decorators import method_decorator

from .models import Slider, FDEnquiry
from .forms import FDEnquiryIntroForm, LGEnquiryForm
from django.utils import timezone
from django.utils.http import urlencode
from django_ratelimit.decorators import ratelimit

from django.shortcuts import redirect
from django.urls import reverse
from django.views import View


class IndexView(View):
    def get(self, request):
        context = {
            "is_index": True,
        }
        return render(request, "web/index.html", context)


class LittleGenieView(View):
    def get(self, request):
        sliders = Slider.objects.filter(is_active=True)
        slider_texts = [i.title for i in sliders]
        slider_subjects = [i.subject for i in sliders]
        form = LGEnquiryForm(request.POST or None)
        context = {
            "slider_texts": slider_texts,
            "slider_subjects": slider_subjects,
            "form": form,
        }
        return render(request, "web/littlegenie.html", context)

    @method_decorator(ratelimit(key="ip", rate="3/m", block=True))
    def post(self, request):
        # if request.POST.get("xaddressx"):
        #     print("Honeypot field filled")
        #     return redirect("web:index")
        form = LGEnquiryForm(request.POST or None)
        context = {}
        if form.is_valid():
            print(form.cleaned_data)
            data = form.save(commit=False)
            data.phone_number = f"+{form.cleaned_data.get('intro_phone_number_country_code')}-{data.phone_number}"
            data.whatsapp_number = f"+{form.cleaned_data.get('intro_whatsapp_number_country_code')}-{data.whatsapp_number}"
            data.utm_source = request.session.get("utm_source", "")
            data.utm_medium = request.session.get("utm_medium", "")
            data.utm_campaign = request.session.get("utm_campaign", "")
            data.utm_content = request.session.get("utm_content", "")
            data.utm_term = request.session.get("utm_term", "")
            # if entry with same phone_number within last 72 hours, then don't save and show error message to user
            if FDEnquiry.objects.filter(phone_number=data.phone_number, timestamp__gte=timezone.now() - timezone.timedelta(hours=72)).exists():
                form.add_error(None, "You have already submitted your details. We will get back to you soon.")
                print("Enquiry already exists")
                context = {"form": form}
                return render(request, "web/thanks.html", context)
            else:
                data.save()
                print("Enquiry saved")
                # send_lead_to_crm(data)
            params = {"origin": request.path}
            return redirect(f"{reverse('web:thanks')}?{urlencode(params)}")
        else:
            return redirect(f"{reverse('web:thanks')}?error=1")


class FoundationView(View):
    def get(self, request):
        form_a = FDEnquiryIntroForm(request.POST or None, prefix="a")
        form_b = FDEnquiryIntroForm(request.POST or None, prefix="b")
        sliders = Slider.objects.filter(is_active=True)
        context = {
            "form_a": form_a,
            "form_b": form_b,
            "sliders": sliders,
            "is_foundation": True,
            "slider_texts" : [i.title for i in sliders],
            "slider_subjects": [i.subject for i in sliders],
        }
        return render(request, "web/foundation.html", context)

    @method_decorator(ratelimit(key="ip", rate="3/m", block=True))
    def post(self, request):
        # if request.POST.get("xaddressx"):
        #     print("Honeypot field filled")
        #     return redirect("web:index")
        prefix = "a" if "a-phone_number" in request.POST else "b"
        form = FDEnquiryIntroForm(request.POST, prefix=prefix)
        context = {}
        if form.is_valid():
            print(form.cleaned_data)
            data = form.save(commit=False)
            data.phone_number = f"+{form.cleaned_data.get('intro_phone_number_country_code')}-{data.phone_number}"
            data.whatsapp_number = f"+{form.cleaned_data.get('intro_whatsapp_number_country_code')}-{data.whatsapp_number}"
            data.utm_source = request.session.get("utm_source", "")
            data.utm_medium = request.session.get("utm_medium", "")
            data.utm_campaign = request.session.get("utm_campaign", "")
            data.utm_content = request.session.get("utm_content", "")
            data.utm_term = request.session.get("utm_term", "")
            # if entry with same phone_number within last 72 hours, then don't save and show error message to user
            if FDEnquiry.objects.filter(phone_number=data.phone_number, timestamp__gte=timezone.now() - timezone.timedelta(hours=72)).exists():
                form.add_error(None, "You have already submitted your details. We will get back to you soon.")
                print("Enquiry already exists")
                context = {"form_a": form if prefix == "a" else FDEnquiryIntroForm(prefix="a"),
                       "form_b": form if prefix == "b" else FDEnquiryIntroForm(prefix="b")}
                return render(request, "web/thanks.html", context)
            else:
                data.save()
                print("Enquiry saved")
                # send_lead_to_crm(data)
            params = {"origin": request.path}
            return redirect(f"{reverse('web:thanks')}?{urlencode(params)}")
        else:
            return redirect(f"{reverse('web:thanks')}?error=1")


class ThanksView(View):
    def get(self, request):
        context = {}
        return render(request, "web/thanks.html", context)
