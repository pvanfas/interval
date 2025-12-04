from decimal import Decimal

import razorpay
from django.conf import settings
from django.core.paginator import Paginator
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.http import urlencode
from django.views.decorators.csrf import csrf_exempt
from smartest.forms import TestLinkForm
from smartest.models import TestLink
from django_ratelimit.decorators import ratelimit

from .forms import ContactDataForm, DemoRequestForm, EnquiryPopupForm, PaymentForm
from .models import (
    AGEGROUP_CHOICES,
    FAQ,
    AcademicProgram,
    Achievement,
    Blog,
    BlogCategory,
    Board,
    City,
    ContactData,
    Country,
    Coupon,
    DemoRequest,
    Enquiry,
    GeneralFeature,
    Location,
    MediaFeature,
    News,
    NonAcademicProgram,
    Payment,
    Resource,
    Slider,
    Staff,
    Subject,
    Testimonial,
)
from .utils import send_demorequest_to_crm, send_lead_to_crm

client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
client.set_app_details({"title": "INTERVAL TALENT BOOST", "version": "1.0"})


def index(request):
    # Use cache key for index page data with version for cache invalidation
    cache_key = "index_page_data_v2"
    cached_data = cache.get(cache_key)

    if cached_data is None:
        # Optimize queries by fetching only needed fields and using select_related
        faqs = list(FAQ.objects.filter(is_active=True).only("question", "answer"))
        achievements = list(Achievement.objects.filter(is_active=True).only("title", "image"))
        newses = list(News.objects.filter(is_active=True).only("title", "slug", "date", "summary", "image")[:6])
        testimonials = list(Testimonial.objects.filter(is_active=True).only("name", "designation", "image", "content", "video_id"))
        media_features = list(MediaFeature.objects.filter(is_active=True).only("title", "image"))
        sliders = list(Slider.objects.filter(is_active=True).only("title", "image").order_by("id"))
        features = list(GeneralFeature.objects.filter(is_active=True).only("title", "description"))

        # Pre-compute slider data to avoid repeated iterations in template
        slider_texts = [i.title for i in sliders]
        slider_images = [i.image.url if i.image else "" for i in sliders]
        first_slider = sliders[0] if sliders else None

        cached_data = {
            "faqs": faqs,
            "achievements": achievements,
            "newses": newses,
            "testimonials": testimonials,
            "media_features": media_features,
            "sliders": sliders,
            "slider_texts": slider_texts,
            "slider_images": slider_images,
            "features": features,
            "first_slider": first_slider,
        }
        # Cache for 10 minutes (increased from 5 for better performance)
        cache.set(cache_key, cached_data, 600)

    context = {"is_index": True, **cached_data}
    return render(request, "web/index.html", context)


def about(request):
    newses = News.objects.filter(is_active=True)[:6]
    staffs = Staff.objects.filter(is_active=True)
    context = {"newses": newses, "staffs": staffs}
    return render(request, "web/about.html", context)


def tools(request):
    context = {}
    return render(request, "web/tools.html", context)


def academic_courses(request):
    academic_courses = AcademicProgram.objects.filter(is_active=True, program_type="ACADEMIC")
    context = {"academic_courses": academic_courses}
    return render(request, "web/courses.html", context)


def language_courses(request):
    academic_courses = AcademicProgram.objects.filter(is_active=True, program_type="LANGUAGE")
    context = {"academic_courses": academic_courses}
    return render(request, "web/courses.html", context)


def nonacademics(request):
    non_academic_courses = NonAcademicProgram.objects.filter(is_active=True, program_type="NON_ACADEMIC")
    context = {"non_academic_courses": non_academic_courses, "agegroups": AGEGROUP_CHOICES}
    return render(request, "web/nonacademics.html", context)


def clubs(request):
    club_courses = NonAcademicProgram.objects.filter(is_active=True, program_type="CLUB")
    context = {"club_courses": club_courses, "agegroups": AGEGROUP_CHOICES}
    return render(request, "web/clubs.html", context)


def news(request):
    newses = News.objects.filter(is_active=True)
    context = {"newses": newses}
    return render(request, "web/news.html", context)


def testimonials(request):
    testimonials = Testimonial.objects.filter(is_active=True)
    context = {"testimonials": testimonials}
    return render(request, "web/testimonials.html", context)


def blogs(request):
    blogs = Blog.objects.filter(is_active=True)
    active_category_slug = request.GET.get("category")
    if active_category_slug:
        active_category = get_object_or_404(BlogCategory, slug=active_category_slug)
        blogs = blogs.filter(category=active_category)
    else:
        active_category = None
    paginator = Paginator(blogs, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    categories = BlogCategory.objects.filter(is_active=True)
    context = {"blogs": page_obj, "categories": categories, "active_category": active_category}
    return render(request, "web/blogs.html", context)


def countries(request):
    context = {
        "countries": Country.objects.filter(is_active=True),
    }
    return render(request, "web/countries.html", context)


def downloads(request):
    resources = Resource.objects.filter(is_active=True)
    context = {"resources": resources}
    return render(request, "web/downloads.html", context)


def terms_and_conditions(request):
    context = {}
    return render(request, "web/terms_and_conditions.html", context)


def privacy_policy(request):
    context = {}
    return render(request, "web/privacy_policy.html", context)


def course_detail(request, slug):
    course = get_object_or_404(AcademicProgram, slug=slug)
    context = {"course": course}
    return render(request, "web/course_detail.html", context)


def nac_course_detail(request, slug):
    course = get_object_or_404(NonAcademicProgram, slug=slug)
    context = {"course": course}
    return render(request, "web/nac_course_detail.html", context)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    related_posts = News.objects.filter(is_active=True).exclude(slug=slug)[:6]
    context = {"news": news, "related_posts": related_posts}
    return render(request, "web/news_detail.html", context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    previous_post = Blog.objects.filter(is_active=True).order_by("date").filter(date__lt=blog.date).last()
    next_post = Blog.objects.filter(is_active=True).order_by("date").filter(date__gt=blog.date).first()
    related_posts = Blog.objects.filter(is_active=True, category=blog.category).exclude(slug=slug)[:6]
    categories = BlogCategory.objects.filter(is_active=True)
    context = {"blog": blog, "previous_post": previous_post, "next_post": next_post, "related_posts": related_posts, "categories": categories}
    template_name = blog.template or "web/blog_detail.html"
    return render(request, template_name, context)


def location_detail(request, slug):
    location = get_object_or_404(Location, slug=slug)
    achievements = Achievement.objects.filter(is_active=True)
    testimonials = Testimonial.objects.filter(is_active=True)
    faqs = FAQ.objects.filter(is_active=True)
    newses = News.objects.filter(is_active=True)[:6]
    features = GeneralFeature.objects.filter(is_active=True)
    context = {"location": location, "achievements": achievements, "testimonials": testimonials, "faqs": faqs, "newses": newses, "features": features}
    template_name = location.template or "web/location_detail.html"
    return render(request, template_name, context)


def subjects(request):
    subjects = Subject.objects.filter(is_active=True)
    faqs = FAQ.objects.filter(is_active=True)
    context = {"subjects": subjects, "faqs": faqs}
    return render(request, "web/subjects.html", context)


def subject_detail(request, slug):
    subject = get_object_or_404(Subject, slug=slug)
    faqs = FAQ.objects.filter(is_active=True)
    context = {"subject": subject, "faqs": faqs}
    return render(request, "web/subject_detail.html", context)


def boards(request):
    boards = Board.objects.filter(is_active=True)
    context = {"boards": boards}
    return render(request, "web/boards.html", context)


def blog_category_detail(request, slug):
    active_category = get_object_or_404(BlogCategory, slug=slug)
    categories = BlogCategory.objects.filter(is_active=True)
    blogs = Blog.objects.filter(category=active_category)
    context = {"active_category": active_category, "blogs": blogs, "categories": categories}
    return render(request, "web/blogs.html", context)


def city_detail(request, slug):
    city = get_object_or_404(City, slug=slug)
    context = {"city": city}
    template_name = "web/city_detail.html"
    return render(request, template_name, context)


def board_detail(request, slug):
    board = get_object_or_404(Board, slug=slug)
    context = {"board": board}
    template_name = "web/board_detail.html"
    return render(request, template_name, context)


def course_form(request, slug):
    form = PaymentForm(request.POST or None)
    course = get_object_or_404(NonAcademicProgram, slug=slug)
    if request.method == "POST":
        if request.POST.get("xaddressx"):
            print("Honeypot field filled")
            return redirect("web:index")
        if form.is_valid():
            data = form.save(commit=False)
            data.course = course
            data.amount = course.course_fee
            data.save()
            return redirect("web:course_payment", pk=data.pk)
        else:
            print(form.errors)
    context = {
        "course": course,
        "form": form,
    }
    return render(request, "web/course_form.html", context)


def course_payment(request, pk):
    payment_obj = get_object_or_404(Payment, pk=pk)
    if payment_obj.is_paid:
        return redirect("web:payment_callback", pk=payment_obj.pk)
    coupon_code = request.GET.get("coupon_code")
    coupon_obj = None
    if coupon_code:
        code = request.GET.get("coupon_code").upper()
        if Coupon.objects.filter(code=code, is_active=True).exists():
            message = "Coupon code is valid"
            if payment_obj.course in Coupon.objects.get(code=code).applicable_courses.all():
                coupon_obj = Coupon.objects.get(code=code)
                discount_amount = round(Decimal(payment_obj.course.course_fee * coupon_obj.discount / 100), 2)
                message = f"Congratulations! You are eligible for a discount of {coupon_obj.discount}% (₹{discount_amount})"
            else:
                message = "Coupon code is not valid for this course"
        else:
            message = "Coupon code is not valid"
    else:
        message = ""

    if coupon_obj:
        discount_amount = Decimal(payment_obj.course.course_fee * coupon_obj.discount / 100)
        payment_obj.coupon = coupon_obj
        payment_obj.discount_amount = discount_amount
        payment_obj.save()
    else:
        payment_obj.discount_amount = 0
        payment_obj.save()

    amount = float(payment_obj.course.course_fee - payment_obj.discount_amount)
    if amount < 1:
        amount = 1
    amount = round(amount, 2)
    session_id = request.session.session_key
    razorpay_order = client.order.create({"amount": amount * 100, "currency": "INR", "payment_capture": "0", "receipt": session_id})
    payment_obj.razorpay_order_id = razorpay_order["id"]
    payment_obj.save()
    relative_url = reverse("web:payment_callback", kwargs={"pk": payment_obj.pk})
    callback_url = request.build_absolute_uri(relative_url)
    print(callback_url)
    context = {
        "coupon_obj": coupon_obj,
        "message": message,
        "course": payment_obj.course,
        "payment_obj": payment_obj,
        "razorpay_order": razorpay_order,
        "amount": amount,
        "razorpay_merchant_key": settings.RAZORPAY_API_KEY,
        "pay_amount": int(amount),
        "razorpay_amount": int(amount * 100),
        "currency": "INR",
        "razorpay_order_id": payment_obj.razorpay_order_id,
        "callback_url": callback_url,
    }
    return render(request, "web/course_payment.html", context)


@csrf_exempt
def payment_callback(request, pk):
    payment_obj = get_object_or_404(Payment, pk=pk)
    context = {"payment_obj": payment_obj}
    print(request.POST)
    if request.method == "POST":
        razorpay_payment_id = request.POST.get("razorpay_payment_id")
        razorpay_order_id = request.POST.get("razorpay_order_id")
        razorpay_signature = request.POST.get("razorpay_signature")
        params_dict = {
            "razorpay_order_id": razorpay_order_id,
            "razorpay_payment_id": razorpay_payment_id,
            "razorpay_signature": razorpay_signature,
        }
        result = client.utility.verify_payment_signature(params_dict)
        if result:
            payment_obj.razorpay_payment_id = razorpay_payment_id
            payment_obj.razorpay_signature = razorpay_signature
            payment_obj.is_paid = True
            payment_obj.paid_at = timezone.now()
            payment_obj.save()
            print(payment_obj.razorpay_payment_id)
            return render(request, "web/payment_callback.html", context)
    return render(request, "web/payment_callback.html", context)


@ratelimit(key="ip", rate="3/m", block=True)
def contact(request):
    form = ContactDataForm(request.POST or None)
    if request.method == "POST":
        if request.POST.get("xaddressx"):
            print("Honeypot field filled")
            return redirect("web:index")
        if form.is_valid():
            data = form.save(commit=False)
            data.phone_number = f"+{form.cleaned_data.get('phone_number_country_code')}-{data.phone_number}"
            data.whatsapp_number = f"+{form.cleaned_data.get('whatsapp_number_country_code')}-{data.whatsapp_number}"
            data.utm_source = request.session.get("utm_source", "")
            data.utm_medium = request.session.get("utm_medium", "")
            data.utm_campaign = request.session.get("utm_campaign", "")
            data.utm_content = request.session.get("utm_content", "")
            data.utm_term = request.session.get("utm_term", "")
            # if entry with same phone_number within last 72 hours, then don't save and show error message to user
            if ContactData.objects.filter(phone_number=data.phone_number, timestamp__gte=timezone.now() - timezone.timedelta(hours=72)).exists():
                form.add_error(None, "You have already submitted your details. We will get back to you soon.")
                context = {"form": form}
                return render(request, "web/contact.html", context)
            else:
                data.save()
                send_lead_to_crm(data)
                return redirect("web:thanks")
        else:
            print(form.errors)
    context = {"form": form}
    return render(request, "web/contact.html", context)


@ratelimit(key="ip", rate="3/m", block=True)
def save_booking(request):
    form = DemoRequestForm(request.POST or None)
    if request.method == "POST":
        if request.POST.get("xaddressx"):
            print("Honeypot field filled")
            return redirect("web:index")
        if form.is_valid():
            print(form.cleaned_data)
            data = form.save(commit=False)
            data.phone_number = f"+{form.cleaned_data.get('demo_phone_number_country_code')}-{data.phone_number}"
            data.whatsapp_number = f"+{form.cleaned_data.get('demo_whatsapp_number_country_code')}-{data.whatsapp_number}"
            data.utm_source = request.session.get("utm_source", "")
            data.utm_medium = request.session.get("utm_medium", "")
            data.utm_campaign = request.session.get("utm_campaign", "")
            data.utm_content = request.session.get("utm_content", "")
            data.utm_term = request.session.get("utm_term", "")
            # if entry with same phone_number within last 72 hours, then don't save and show error message to user
            if DemoRequest.objects.filter(phone_number=data.phone_number, timestamp__gte=timezone.now() - timezone.timedelta(hours=72)).exists():
                form.add_error(None, "You have already submitted your details. We will get back to you soon.")
                context = {"form": form}
                return render(request, "web/contact.html", context)
            else:
                data.save()
                send_demorequest_to_crm(data)
            params = {"model": "DemoRequest", "token": data.token}
            return redirect(f"{reverse('web:verify')}?{urlencode(params)}")
        else:
            print(form.errors)
    return redirect("web:index")


@ratelimit(key="ip", rate="3/m", block=True)
def thanks(request):
    print("Thanks page")
    if request.method == "POST":
        if request.POST.get("xaddressx"):
            print("Honeypot field filled")
            return redirect("web:index")
    form = EnquiryPopupForm(request.POST or None)
    context = {}
    if form.is_valid():
        print(form.cleaned_data)
        data = form.save(commit=False)
        data.phone_number = f"+{form.cleaned_data.get('popup_phone_number_country_code')}-{data.phone_number}"
        data.whatsapp_number = f"+{form.cleaned_data.get('popup_whatsapp_number_country_code')}-{data.whatsapp_number}"
        data.utm_source = request.session.get("utm_source", "")
        data.utm_medium = request.session.get("utm_medium", "")
        data.utm_campaign = request.session.get("utm_campaign", "")
        data.utm_content = request.session.get("utm_content", "")
        data.utm_term = request.session.get("utm_term", "")
        # if entry with same phone_number within last 72 hours, then don't save and show error message to user
        if Enquiry.objects.filter(phone_number=data.phone_number, timestamp__gte=timezone.now() - timezone.timedelta(hours=72)).exists():
            form.add_error(None, "You have already submitted your details. We will get back to you soon.")
            print("Enquiry already exists")
            context = {"form": form}
            return render(request, "web/thanks.html", context)
        else:
            data.save()
            print("Enquiry saved")
            send_lead_to_crm(data)
        params = {"model": "Enquiry", "token": data.token}
        return redirect(f"{reverse('web:verify')}?{urlencode(params)}")
    else:
        print(form.errors)
    return render(request, "web/thanks.html", context)


def verify(request):
    model = request.GET.get("model")
    token = request.GET.get("token")
    if model == "DemoRequest":
        obj = get_object_or_404(DemoRequest, token=token)
    elif model == "Enquiry":
        obj = get_object_or_404(Enquiry, token=token)
    elif model == "Contact":
        obj = get_object_or_404(ContactData, token=token)
    else:
        obj = None
    thanks_url = reverse("web:thanks")
    return redirect(f"{thanks_url}?weblead_id={token}")
    # context = {"model": model, "obj": obj}
    # return render(request, "web/verify.html", context)


def smartest_search(request):
    form = TestLinkForm(request.POST or None)
    params = {
        "board": request.GET.get("board"),
        "standard": request.GET.get("standard"),
        "subject": request.GET.get("subject"),
    }
    for key, value in params.items():
        if value:
            form.initial[key] = value
    tests = None
    if all(params.values()):
        tests = TestLink.objects.filter(**params)
    context = {"form": form, "tests": tests}
    return render(request, "web/smartest/search.html", context)


def kerala_sslc_calculator(request):
    return render(request, "web/tools/kerala_sslc_calculator.html")


def tamilnadu_sslc_calculator(request):
    return render(request, "web/tools/tamilnadu_sslc_calculator.html")


def cbse_calculator(request):
    return render(request, "web/tools/cbse_calculator.html")


def cbse_calculator_12(request):
    return render(request, "web/tools/cbse_calculator_12.html")


def kerala_hsc_calculator(request):
    return render(request, "web/tools/kerala_hsc_calculator.html")


def tamilnadu_hsc_calculator(request):
    return render(request, "web/tools/tamilnadu_hsc_calculator.html")


def bad_request(request, exception, template_name="400.html"):
    """
    Custom 400 error handler that includes request in context
    so that context processors can run.
    """
    response = render(request, template_name)
    response.status_code = 400
    return response


def permission_denied(request, exception, template_name="403.html"):
    """
    Custom 403 error handler that includes request in context
    so that context processors can run.
    """
    response = render(request, template_name)
    response.status_code = 403
    return response


def page_not_found(request, exception, template_name="404.html"):
    """
    Custom 404 error handler that includes request in context
    so that context processors can run.
    """
    response = render(request, template_name)
    response.status_code = 404
    return response


def server_error(request, template_name="500.html"):
    """
    Custom 500 error handler that includes request in context
    so that context processors can run.
    """
    response = render(request, template_name)
    response.status_code = 500
    return response
