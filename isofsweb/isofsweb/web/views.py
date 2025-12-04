from django.shortcuts import redirect, render, get_object_or_404

from .forms import ApplicationForm, ChatRequestForm, PhoneRequestForm, CourseEnquiryForm
from .models import FAQ, Course, IndustryExpert, SkillCategory, Testimonial


def index(request):
    context = {
        "is_index": True,
        "industry_experts": IndustryExpert.objects.all(),
        "courses": Course.objects.all(),
        "testimonials": Testimonial.objects.all(),
        "faqs": FAQ.objects.all(),
    }
    return render(request, "web/index.html", context)



def admissions(request):
    admission_form = ApplicationForm()
    context = {
        "is_admissions": True,
        "industry_experts": IndustryExpert.objects.all(),
        "admission_form": admission_form,
    }
    return render(request, "web/admissions.html", context)




def about_us(request):
    context = {
        "is_about_us": True,
        "industry_experts": IndustryExpert.objects.all(),
    }
    return render(request, "web/about_us.html", context)


def program_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    form = CourseEnquiryForm()
    if request.method == "POST":
        form = CourseEnquiryForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.course = course
            data.save()
            return redirect("web:success")
    context = {
        "course": course,
        "form": form,
        "industry_experts": IndustryExpert.objects.all(),
    }
    return render(request, "web/program_detail.html", context)


def save_application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("web:success")
        else:
            print(form.errors)
    return redirect("web:index")


def save_chat_request(request):
    if request.method == "POST":
        form = ChatRequestForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("web:success")
        else:
            print(form.errors)
    return redirect("web:index")


def save_phone_request(request):
    if request.method == "POST":
        form = PhoneRequestForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("web:success")
        else:
            print(form.errors)
    return redirect("web:index")


def success(request):
    return render(request, "web/success.html", {})


def pricing_policy(request):
    return render(request, "web/pricing_policy.html", {})


def shipping_policy(request):
    return render(request, "web/shipping_policy.html", {})


def terms_and_conditions(request):
    return render(request, "web/terms_and_conditions.html", {})


def privacy_policy(request):
    return render(request, "web/privacy_policy.html", {})


def cancellation_refund_policy(request):
    return render(request, "web/cancellation_refund_policy.html", {})


def payment_policy(request):
    return render(request, "web/payment_policy.html", {})


def success_stories(request):
    context = {
        "is_success_stories": True,
        "testimonials": Testimonial.objects.all(),
    }
    return render(request, "web/success_stories.html", context)


def our_centers(request):
    context = {
        "is_our_centers": True,
    }
    return render(request, "web/our_centers.html", context)


def contact(request):
    context = {
        "is_contact": True,
    }
    return render(request, "web/contact.html", context)


def resources(request):
    context = {
        "is_resources": True,
        "skill_categories": SkillCategory.objects.all(),
        "courses": Course.objects.all(),
        "industry_experts": IndustryExpert.objects.all(),
    }
    return render(request, "web/resources.html", context)
