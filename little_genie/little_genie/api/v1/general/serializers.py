from core.models import FAQ
from core.models import About
from core.models import Contact
from core.models import Feature
from core.models import Gallery
from core.models import Social
from core.models import Testimonial
from course.models import CourseEnquiry
from products.models import ProductEnquiry
from rest_framework import serializers


class CourseEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnquiry
        fields = "__all__"


class ProductEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEnquiry
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ("is_checked",)


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"


class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ["timestamp", "is_checked"]


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"
