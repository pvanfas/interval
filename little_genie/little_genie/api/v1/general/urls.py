from core.models import FAQ
from core.models import Feature
from core.models import Gallery
from core.models import Social
from core.models import Testimonial
from django.urls import path
from rest_framework.generics import ListAPIView

from . import views
from .serializers import FAQSerializer
from .serializers import FeatureSerializer
from .serializers import GallerySerializer
from .serializers import SocialSerializer
from .serializers import TestimonialSerializer


app_name = "general"

urlpatterns = [
    path("about/", views.AboutView.as_view()),
    path("gallery/", ListAPIView.as_view(queryset=Gallery.objects.all(), serializer_class=GallerySerializer)),
    path(
        "testimonials/", ListAPIView.as_view(queryset=Testimonial.objects.all(), serializer_class=TestimonialSerializer)
    ),
    path("features/", ListAPIView.as_view(queryset=Feature.objects.all(), serializer_class=FeatureSerializer)),
    path("socials/", ListAPIView.as_view(queryset=Social.objects.all(), serializer_class=SocialSerializer)),
    path("faq/", ListAPIView.as_view(queryset=FAQ.objects.all(), serializer_class=FAQSerializer)),
    path("create-contact/", views.CreateContact.as_view()),
    path("product-enquiry/", views.ProductEnquiry.as_view()),
    path("course-enquiry/", views.CourseEnquiry.as_view()),
]
