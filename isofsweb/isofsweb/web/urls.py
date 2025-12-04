from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("admissions/", views.admissions, name="admissions"),
    path("about/", views.about_us, name="about_us"),
    path("program/<str:slug>/", views.program_detail, name="program_detail"),
    # Form save views
    path("form/save_application/", views.save_application, name="save_application"),
    path("form/save_chat_request/", views.save_chat_request, name="save_chat_request"),
    path("form/save_phone_request/", views.save_phone_request, name="save_phone_request"),
    path("form/success/", views.success, name="success"),
    # Policies
    path("pricing-policy/", views.pricing_policy, name="pricing_policy"),
    path("shipping-policy/", views.shipping_policy, name="shipping_policy"),
    path("terms-and-conditions/", views.terms_and_conditions, name="terms_and_conditions"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("cancellation-refund-policy/", views.cancellation_refund_policy, name="cancellation_refund_policy"),
    path("payment-policy/", views.payment_policy, name="payment_policy"),
    # Additional pages
    path("success-stories/", views.success_stories, name="success_stories"),
    path("our-centers/", views.our_centers, name="our_centers"),
    path("contact/", views.contact, name="contact"),
    path("resources/", views.resources, name="resources"),
]
