from course.models import Course
from django.urls import path
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from .serializers import CourseSerializer


app_name = "course"

urlpatterns = [
    path("", ListAPIView.as_view(queryset=Course.objects.all(), serializer_class=CourseSerializer)),
    path("<str:pk>/", RetrieveAPIView.as_view(queryset=Course.objects.all(), serializer_class=CourseSerializer)),
]
