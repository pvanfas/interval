import razorpay
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from main.forms import SchoolForm, SchoolPaymentForm, StudentRegistrationForm
from main.models import Coupon, Document, School, StudentRegistration
from main.utils import send_whatsapp_message

client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
client.set_app_details({"title": "INTERVAL TALENT BOOST", "version": "1.0"})


def generate_register_number(instance):
    center_map = {"KOZHIKODE": "K", "ERNAKULAM": "E", "TRIVANDRUM": "T"}
    pec = instance.preferred_exam_centre
    center_code = center_map[pec] if pec in center_map else "B"
    if pec in center_map:
        items = StudentRegistration.objects.filter(preferred_exam_centre=pec, register_number__isnull=False)
    else:
        items = StudentRegistration.objects.filter(register_number__isnull=False).exclude(preferred_exam_centre__in=center_map.keys())
    if not items:
        new_register_number = f"ITB{center_code}101"
        instance.register_number = new_register_number
        instance.save()
        return new_register_number
    else:
        dataset = [int(item.register_number[4:]) for item in items]
        item = items.filter(register_number=f"ITB{center_code}{max(dataset)}").first()
        if item:
            last_number = item.register_number[4:]
            number = int(last_number) + 1
            new_register_number = f"ITB{center_code}{number}"
        else:
            new_register_number = f"ITB{center_code}101"
        instance.register_number = new_register_number
        instance.save()
        return new_register_number


def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)


def about(request):
    return render(request, "web/about.html")


def student_application(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            contact_number_country_code = form.cleaned_data.get("selected_contact_number_country_code")
            whatsapp_country_code = form.cleaned_data.get("selected_whatsapp_country_code")
            contact_number = form.cleaned_data.get("contact_number")
            whatsapp_number = form.cleaned_data.get("whatsapp_number")

            data = form.save(commit=False)
            data.contact_number = f"{contact_number_country_code}{contact_number}"
            data.whatsapp_number = f"{whatsapp_country_code}{whatsapp_number}"
            data.save()
            return redirect(reverse("web:student_payment", kwargs={"pk": data.pk}))
    context = {"registration_form": StudentRegistrationForm()}
    return render(request, "web/thanks.html", context)


def student_payment(request, pk):
    amount = settings.STUDENT_PAYMENT_AMOUNT
    registration = get_object_or_404(StudentRegistration, pk=pk)

    coupon_code = request.GET.get("coupon_code")
    if coupon_code:
        if Coupon.objects.filter(code=coupon_code.upper()).exists():
            coupon = Coupon.objects.get(code=coupon_code.upper())
            registration.coupon = coupon.code
            registration.save()
            amount -= coupon.discount
            message = f"Congratulations! You have successfully applied the coupon code {coupon.code} and got a discount of Rs. {coupon.discount}."
        else:
            message = "Invalid coupon code!"
    else:
        message = None

    if amount == 0:
        context = {"registration": registration, "amount": amount, "message": message}
        context["pay_amount"] = int(amount)
        context["razorpay_amount"] = int(amount * 100)
        context["currency"] = "INR"
        context["callback_url"] = reverse("web:student_callback", kwargs={"pk": registration.pk})
        if request.method == "POST":
            registration.is_paid = True
            registration.paid_at = timezone.now()
            registration.register_number = generate_register_number(registration)
            registration.save()
            send_whatsapp_message(registration)
            return redirect(reverse("web:student_thanks", kwargs={"pk": registration.pk}))

        return render(request, "web/payment.html", context)

    else:
        razorpay_order = client.order.create({"amount": float(amount) * 100, "currency": "INR", "payment_capture": "0", "receipt": registration.register_number})
        registration.razorpay_order_id = razorpay_order["id"]
        registration.save()

        context = {"registration": registration, "razorpay_order": razorpay_order, "amount": amount, "message": message}
        context["razorpay_merchant_key"] = settings.RAZORPAY_API_KEY
        context["pay_amount"] = int(amount)
        context["razorpay_amount"] = int(amount * 100)
        context["currency"] = "INR"
        context["razorpay_order_id"] = registration.razorpay_order_id
        context["callback_url"] = reverse("web:student_callback", kwargs={"pk": registration.pk})
        return render(request, "web/payment.html", context)


@csrf_exempt
def student_callback(request, pk):
    registration = get_object_or_404(StudentRegistration, pk=pk)
    if request.method == "POST":
        razorpay_payment_id = request.POST.get("razorpay_payment_id", "")
        razorpay_order_id = request.POST.get("razorpay_order_id", "")
        razorpay_signature = request.POST.get("razorpay_signature", "")
        params_dict = {
            "razorpay_order_id": razorpay_order_id,
            "razorpay_payment_id": razorpay_payment_id,
            "razorpay_signature": razorpay_signature,
        }
        result = client.utility.verify_payment_signature(params_dict)
        if result:
            registration.razorpay_payment_id = razorpay_payment_id
            registration.razorpay_signature = razorpay_signature
            registration.is_paid = True
            registration.paid_at = timezone.now()
            registration.register_number = generate_register_number(registration)
            registration.save()
            send_whatsapp_message(registration)
            return redirect(reverse("web:student_thanks", kwargs={"pk": registration.pk}))
        else:
            return redirect(reverse("web:student_payment", kwargs={"pk": registration.pk}))
    return redirect(reverse("web:student_payment", kwargs={"pk": registration.pk}))


def student_thanks(request, pk):
    registration = get_object_or_404(StudentRegistration, pk=pk)
    return render(request, "web/thanks.html", {"registration": registration})


def school_registration(request):
    model = Document
    if request.method == "POST":
        form = SchoolForm(request.POST, request.FILES or None)
        if form.is_valid():
            data = form.save()
            if request.FILES:
                for f in request.FILES.getlist("file"):
                    obj = model.objects.create(file=f, school=data)
            return redirect(reverse("web:school_payment", kwargs={"pk": data.pk}))
    return render(request, "web/school_registration.html")


def school_payment(request, pk):
    school = get_object_or_404(School, pk=pk)
    context = {"school": school}
    form = SchoolPaymentForm(request.POST or None, request.FILES or None, instance=school)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("web:school_thanks", kwargs={"pk": school.pk}))
    context["form"] = form
    return render(request, "web/school_payment.html", context)


def school_thanks(request, pk):
    school = get_object_or_404(School, pk=pk)
    return render(request, "web/school_thanks.html", {"school": school})
